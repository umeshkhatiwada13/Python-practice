# Initializing the Dictionary and populating with value
semesterData = {
    "COM 3013": "Olga",
    "CBD 2214": "Graham Wall",
    "AML 1301": "Peter S.",
    "AML 1114": "Amir S.",
    "AML 1214": "Parwinder Kaur",
    "AML 1413": "Ashish G."
}

print("Original Dictionary {}".format(semesterData))

# Changing name of course COM 3013 from Olga to Sergio Ramos
semesterData["COM 3013"] = 'Sergio Ramos'

print("Dictionary after changing COM 3013 instructor : {}".format(semesterData))
