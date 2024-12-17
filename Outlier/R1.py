import gurobipy as gp
from gurobipy import GRB

# Original Data
data = {'capacity_in_supplier': {'supplier1': 150, 'supplier2': 50, 'supplier3': 100},
        'shipping_cost_from_supplier_to_roastery': {('supplier1', 'roastery1'): 5, ('supplier1', 'roastery2'): 4,
                                                    ('supplier2', 'roastery1'): 6, ('supplier2', 'roastery2'): 3,
                                                    ('supplier3', 'roastery1'): 2, ('supplier3', 'roastery2'): 7},
        'roasting_cost_light': {'roastery1': 3, 'roastery2': 5}, 'roasting_cost_dark': {'roastery1': 5, 'roastery2': 6},
        'shipping_cost_from_roastery_to_cafe': {('roastery1', 'cafe1'): 5, ('roastery1', 'cafe2'): 3,
                                                ('roastery1', 'cafe3'): 6, ('roastery2', 'cafe1'): 4,
                                                ('roastery2', 'cafe2'): 5, ('roastery2', 'cafe3'): 2},
        'light_coffee_needed_for_cafe': {'cafe1': 20, 'cafe2': 30, 'cafe3': 40},
        'dark_coffee_needed_for_cafe': {'cafe1': 20, 'cafe2': 20, 'cafe3': 100}, 'cafes': ['cafe3', 'cafe2', 'cafe1'],
        'roasteries': ['roastery2', 'roastery1'], 'suppliers': ['supplier3', 'supplier1', 'supplier2']}

# Understanding the changes and generating the new data
# The only change in the data is the demand for light coffee at cafe2, which increases by 29%.
new_data = data.copy()  # Create a copy to avoid modifying the original data
new_data['light_coffee_needed_for_cafe']['cafe2'] = round(data['light_coffee_needed_for_cafe']['cafe2'] * 1.29)

print("Understanding the New Data:")
print("The demand for light coffee at cafe2 has increased by 29%, from 30 to",
      new_data['light_coffee_needed_for_cafe']['cafe2'])
print("\nNew Data:")
print(new_data)

# Gurobipy Model
model = gp.Model("Coffee_Supply_Chain")

# Decision Variables

# Amount of coffee beans sourced from each supplier
source = model.addVars(new_data['suppliers'], new_data['roasteries'], vtype=GRB.CONTINUOUS, name="source")

# Amount of light/dark coffee roasted at each roastery
roast_light = model.addVars(new_data['roasteries'], vtype=GRB.CONTINUOUS, name="roast_light")
roast_dark = model.addVars(new_data['roasteries'], vtype=GRB.CONTINUOUS, name="roast_dark")

# Amount of light/dark coffee shipped from each roastery to each cafe
ship_light = model.addVars(new_data['roasteries'], new_data['cafes'], vtype=GRB.CONTINUOUS, name="ship_light")
ship_dark = model.addVars(new_data['roasteries'], new_data['cafes'], vtype=GRB.CONTINUOUS, name="ship_dark")

# Constraints

# Supplier Capacity Constraint
for supplier in new_data['suppliers']:
    model.addConstr(source.sum(supplier, '*') <= new_data['capacity_in_supplier'][supplier],
                    name=f"supplier_capacity_{supplier}")

# Demand Constraints
for cafe in new_data['cafes']:
    model.addConstr(ship_light.sum('*', cafe) == new_data['light_coffee_needed_for_cafe'][cafe],
                    name=f"demand_light_{cafe}")
    model.addConstr(ship_dark.sum('*', cafe) == new_data['dark_coffee_needed_for_cafe'][cafe],
                    name=f"demand_dark_{cafe}")

# Roasting Input/Output Constraint
for roastery in new_data['roasteries']:
    model.addConstr(roast_light[roastery] == ship_light.sum(roastery, '*'), name=f"roast_light_balance_{roastery}")
    model.addConstr(roast_dark[roastery] == ship_dark.sum(roastery, '*'), name=f"roast_dark_balance_{roastery}")

# Roasting Input = Sourcing from Suppliers Constraint
for roastery in new_data['roasteries']:
    model.addConstr(source.sum('*', roastery) == roast_light[roastery] + roast_dark[roastery],
                    name=f"sourcing_roasting_balance_{roastery}")

# Objective Function: Minimize Total Cost
total_shipping_supplier_roastery = gp.quicksum(
    new_data['shipping_cost_from_supplier_to_roastery'][supplier, roastery] * source[supplier, roastery] for
    supplier, roastery in new_data['shipping_cost_from_supplier_to_roastery'])
total_roasting_cost = gp.quicksum(
    new_data['roasting_cost_light'][roastery] * roast_light[roastery] + new_data['roasting_cost_dark'][roastery] *
    roast_dark[roastery] for roastery in new_data['roasteries'])
total_shipping_roastery_cafe = gp.quicksum(new_data['shipping_cost_from_roastery_to_cafe'][roastery, cafe] * (
            ship_light[roastery, cafe] + ship_dark[roastery, cafe]) for roastery, cafe in
                                           new_data['shipping_cost_from_roastery_to_cafe'])

model.setObjective(total_shipping_supplier_roastery + total_roasting_cost + total_shipping_roastery_cafe, GRB.MINIMIZE)

# Solve the model
model.optimize()

# Print results
if model.status == GRB.OPTIMAL:
    print("\nOptimal Solution:")
    for v in model.getVars():
        print(f"{v.varName}: {v.x} (Lower Bound: {v.SAObjLow}, Upper Bound: {v.SAObjUp})")
    print("\nTotal Cost:", model.objVal)
else:
    print("No optimal solution found.")




