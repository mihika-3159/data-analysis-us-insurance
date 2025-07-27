import csv
ages=[]
sexes=[]
bmis=[]
children=[]
smoker_statuses=[]
regions=[]
charges=[]
with open('insurance.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ages.append(row["age"])
        sexes.append(row["sex"])
        bmis.append(row["bmi"])
        children.append(row["children"])
        smoker_statuses.append(row["smoker"])
        regions.append(row["region"])
        charges.append(row["charges"])
def avg_age():
    return sum(int(age) for age in ages) / len(ages)
def avg_bmi():
    return sum(float(bmi) for bmi in bmis) / len(bmis)
def avg_children():
    return sum(int(child) for child in children) / len(children)
def avg_charges():
    return sum(float(charge) for charge in charges) / len(charges)
def smoker_percentage():
    smokers = sum(1 for smoker in smoker_statuses if smoker.lower() == 'yes')
    return (smokers / len(smoker_statuses)) * 100
def region_distribution():
    distribution = {}
    for region in regions:
        if region in distribution:
            distribution[region] += 1
        else:
            distribution[region] = 1
    return distribution
def smoker_to_region():
    smoker_regions = {}
    for i in range(len(smoker_statuses)):
        if smoker_statuses[i].lower() == 'yes':
            region = regions[i]
            if region in smoker_regions:
                smoker_regions[region] += 1
            else:
                smoker_regions[region] = 1
    return smoker_regions
def region_charges():
    region_charges = {}
    for i in range(len(regions)):
        region = regions[i]
        charge = float(charges[i])
        if region in region_charges:
            region_charges[region].append(charge)
        else:
            region_charges[region] = [charge]
    return {region: sum(charges) / len(charges) for region, charges in region_charges.items()}
def children_to_region():
    children_regions = {}
    for i in range(len(children)):
        region = regions[i]
        child_count = int(children[i])
        if region in children_regions:
            children_regions[region] += child_count
        else:
            children_regions[region] = child_count
    return children_regions
def sex_to_region():
    sex_regions = {}
    for i in range(len(sexes)):
        region = regions[i]
        if region not in sex_regions:
            sex_regions[region] = {"Male": 0, "Female": 0}
        if sexes[i].lower()=='male':
            sex_regions[region]["Male"] += 1
        elif sexes[i].lower()=='female':
            sex_regions[region]["Female"] += 1
    return sex_regions
def bmi_to_region():
    bmi_regions = {}
    for i in range(len(bmis)):
        region = regions[i]
        bmi_value = float(bmis[i])
        if region in bmi_regions:
            bmi_regions[region].append(bmi_value)
        else:
            bmi_regions[region] = [bmi_value]
    return {region: sum(bmis) / len(bmis) for region, bmis in bmi_regions.items()}
def smoker_to_sex():
    smoker_to_sex={"Male": 0, "Female": 0}
    for i in range(len(smoker_statuses)):
        if smoker_statuses[i].lower() == 'yes':
            if sexes[i].lower()=='male':
                smoker_to_sex["Male"] += 1
            elif sexes[i].lower()=='female':
                smoker_to_sex["Female"] += 1
    return smoker_to_sex

def main():
    print("Average Age:", avg_age())
    print("Average BMI:", avg_bmi())
    print("Average Number of Children:", avg_children())
    print("Average Charges:", avg_charges())
    print("Percentage of Smokers:", smoker_percentage(), "%")
    print("Region Distribution:", region_distribution())
    print("Smoker Count by Region:", smoker_to_region())
    print("Average Charges by Region:", region_charges())
    print("Total Children by Region:", children_to_region())
    print("Sex Count by Region:", sex_to_region())
    print("Average BMI by Region:", bmi_to_region())
    print("Smoker Count by Sex:", smoker_to_sex())