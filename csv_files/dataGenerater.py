import openai
import random
import datetime
import csv
import sys

# openai.api_key = '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'

def read_menu_from_csv(filename='menu.csv'):
    menu = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Adjust the condition to allow empty menu_type
            if len(row) != 5 or row[0].strip() == '' or row[1].strip() == '' or row[3].strip() == '' or row[4].strip() == '':
                print(f"Skipping invalid or empty row: {row}")
                continue
            try:
                id_, name, type_, price, production_cost = row
                menu.append((int(id_), name, type_, float(price), float(production_cost)))
            except ValueError as e:
                print(f"Error converting row {row}: {e}")
    return menu



def generate_name():
    try:
        response = openai.Completion.create(
          engine="babbage-002",
          prompt="Generate 50 random first and last name.",
          temperature=0.5,
          max_tokens=10,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        name = response.choices[0].text.strip()
        return name
    except openai.error.InvalidRequestError as e:
        print(f"Failed to generate name: {e}")
        return "Name Generation Failed"

def generate_name_from_list():

    names_list = [("Doe, John"), ("Smith, Jane"), ("Brown, Michael"), ("Taylor, Sarah"), ("Wilson, James"),
                ("Johnson, Emily"), ("Williams, David"), ("Jones, Jessica"), ("Miller, Chris"), ("Davis, Amanda"),
                ("Garcia, Matthew"), ("Rodriguez, Ashley"), ("Martinez, Joshua"), ("Hernandez, Sophia"), ("Lopez, Daniel"),
                ("Gonzalez, Olivia"), ("Perez, Nicholas"), ("Sanchez, Elizabeth"), ("Ramirez, Alexander"), ("Flores, Mia"),
                ("Lee, Ethan"), ("Walker, Isabella"), ("Hall, Ryan"), ("Allen, Ava"), ("Young, Jack"),
                ("Hernandez, Charlotte"), ("King, Jacob"), ("Wright, Lily"), ("Lopez, Benjamin"), ("Hill, Emily"),
                ("Scott, Madison"), ("Green, Dylan"), ("Adams, Chloe"), ("Baker, Lucas"), ("Nelson, Kaylee"),
                ("Carter, Logan"), ("Mitchell, Zoe"), ("Perez, Tyler"), ("Roberts, Layla"), ("Turner, Joseph"),
                ("Phillips, Grace"), ("Campbell, Alexander"), ("Parker, Victoria"), ("Evans, Isaiah"), ("Edwards, Aubrey"),
                ("Collins, Gabriel"), ("Stewart, Scarlett"), ("Morris, Samuel"), ("Morales, Sofia"), ("Murphy, Charlie"),
                ("Cook, Bella"), ("Rogers, Isaac"), ("Morgan, Riley"), ("Peterson, Elijah"), ("Cooper, Ellie"),
                ("Reed, Landon"), ("Bailey, Hannah"), ("Bell, Andrew"), ("Gomez, Lily"), ("Kelly, Adrian"),
                ("Howard, Nora"), ("Ward, Mason"), ("Cox, Zoe"), ("Diaz, Max"), ("Richardson, Penelope"),
                ("Wood, Leo"), ("Watson, Layla"), ("Brooks, Aaron"), ("Bennett, Isla"), ("Gray, Theodore"),
                ("James, Maya"), ("Reyes, Ivan"), ("Cruz, Lucy"), ("Hughes, Bryant"), ("Price, Aria"),
                ("Myers, Owen"), ("Long, Harper"), ("Foster, Sebastian"), ("Sanders, Ella"), ("Ross, Gavin"),
                ("Morales, Ariana"), ("Powell, Ian"), ("Sullivan, Savannah"), ("Russell, Christian"), ("Ortiz, Annabelle"),
                ("Jenkins, Colton"), ("Gutierrez, Hailey"), ("Perry, Jaxon"), ("Butler, Trinity"), ("Barnes, Dominic"),
                ("Fisher, Lily"), ("Henderson, Hunter"), ("Coleman, Mackenzie"), ("Simmons, Brayden"), ("Patterson, Julian"),
                ("Jordan, Kinsley"), ("Reynolds, Luca"), ("Hamilton, Naomi"), ("Graham, Kayden"), ("Kim, Alice"),
                ("Gonzales, Jose"), ("Alexander, Madelyn"), ("Ramos, Carter"), ("Wallace, Avery"), ("Griffin, Miles"),
                ("West, Mila"), ("Ford, Silas"), ("Marshall, Brooke"), ("Owens, Micah"), ("Freeman, Paige")]

    return random.choices(names_list)




def generate_random_date_in_2017():
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 12, 31)
    random_number_of_days = random.randrange((end_date - start_date).days)
    return start_date + datetime.timedelta(days=random_number_of_days)

def generate_order_data(num_orders, menus):
    orders = []
    for _ in range(num_orders):
        name = generate_name_from_list()
        # Randomly choose how many items will be in the order (e.g., 1 to 5 items)
        num_items = random.randint(1, 5)
        order_list = random.sample(menus, num_items)
        total_price = sum(item[3] for item in order_list)  # Sum prices of items
        order_date = generate_random_date_in_2017()
        order_ids = ",".join(str(item[0]) for item in order_list)  # Concatenate menu IDs
        orders.append([name, order_ids, f"${total_price:.2f}", order_date])

    return orders

def write_orders_to_csv(orders, filename='orders.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Order List (Menu IDs)', 'Total Price', 'Order Date'])
        writer.writerows(orders)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        menus = read_menu_from_csv()  # Read menu data from CSV
        num_orders = int(sys.argv[1])  # Number of orders from command-line argument
        orders = generate_order_data(num_orders, menus)
        write_orders_to_csv(orders)
    else:
        print("Please specify the number of orders to generate.")
