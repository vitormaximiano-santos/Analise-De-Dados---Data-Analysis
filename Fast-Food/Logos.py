import base64
import os

# Caminho da pasta com as logos
folder = r"C:\Users\Vitor\Desktop\Portifolio\portifolio 01\Logos"

# Mapeamento arquivo → nome correto da empresa (exatamente como está na sua planilha)
names = {
    "Arbys_logo_PNG3.png": "Arby's",
    "Baskin_robbins_logo.PNG.jpg": "Baskin-Robbins",
    "Bojangles-PNG_010.png": "Bojangles",
    "Burger_king_logo_PNG2.png": "Burger King",
    "Carls_Jr._logo_PNG1.png": "Carl's Jr.",
    "Checkers-Rally's.png": "Checkers/Rally's",
    "Chick_fil_A_logo_PNG17.png": "Chick-fil-A",
    "chipotle_logo_PNG1.png": "Chipotle",
    "Churchs-Chicken-Logo.png": "Church's Chicken",
    "Culvers-Logo-2006.png": "Culver's",
    "Dairy_Queen_Logo_PNG4.png": "Dairy Queen",
    "Del_taco.png": "Del Taco",
    "Dominos_logo_PNG1.png": "Domino's",
    "Dunkin_Donuts_logo_PNG8.png": "Dunkin'",
    "El_Pollo_Loco_logo_PNG1.png": "El Pollo Loco",
    "Firehouse-Subs-PNG_005.png": "Firehouse Subs",
    "Five-Guys-Logo-PNG_009.png": "Five Guys",
    "Freddy´s.png": "Freddy's Frozen Custard & Steakburgers",
    "Hardees-Logo-PNG_005.png": "Hardee's",
    "In-N-Out-Burger-Logo-PNG_001.png": "In-N-Out Burger",
    "Jack_in_the_Box_logo_PNG5.png": "Jack in the Box",
    "Jersey-Mikes-Logo.png": "Jersey Mike's",
    "Jimmy_Johns_logo_PNG1.png": "Jimmy John's",
    "kfcPNG.png": "KFC",
    "Krispy_Kreme_logo_PNG6.png": "Krispy Kreme",
    "Little-Caesars-Logo-PNG_005.png": "Little Caesars",
    "Marco's_pizza.png": "Marco's Pizza",
    "MCAlisters.png": "McAlister's Deli",
    "mcdonalds_logo_PNG5.png": "McDonald's",
    "Moe´s.png": "Moe's Southwest Grill",
    "Panda_Express_logo_PNG2.png": "Panda Express",
    "Panera_Bread_logo_PNG5.png": "Panera Bread",
    "Papa_Johns_logo_PNG1.png": "Papa Johns",
    "Papa_Murphy´s.png": "Papa Murphy's",
    "pizza_hut_logo_PNG1.png": "Pizza Hut",
    "Popeyes_logo_PNG3.png": "Popeyes Louisiana Kitchen",
    "QDOBA-Logo-PNG_003.png": "QDOBA",
    "Raising-Canes-Logo.png": "Raising Cane's",
    "Shake-Shack-Logo-PNG_005.png": "Shake Shack",
    "Smoothie-King-PNG_003.png": "Smoothie King",
    "SONIC_New_Logo_2020.png": "Sonic Drive-In",
    "starbucks_logo_PNG3.png": "Starbucks",
    "Subway_logo_PNG16.png": "Subway",
    "Taco_bell_logo_PNG1.png": "Taco Bell",
    "Tim-Hortons-Logo-PNG1.png": "Tim Hortons",
    "tropical-smoothie-cafe-logo.PNG": "Tropical Smoothie Cafe",
    "Wendys_logo_PNG1.png": "Wendy's",
    "Whataburger-Logo-PNG_002.png": "Whataburger",
    "White-Castle-Logo-PNG_001.png": "White Castle",
    "Wingstop-Logo-PNG1.png": "Wingstop",
    "Zaxbys-Logo.png": "Zaxby's"
}

# Arquivo de saída com o SWITCH completo
output_file = r"C:\Users\Vitor\Desktop\LogoURL_SWITCH.txt"

with open(output_file, "w", encoding="utf-8") as out:
    out.write("LogoURL =\nSWITCH(\n    'Logos'[Fast-Food Chains],\n")

    for filename, display_name in names.items():
        filepath = os.path.join(folder, filename)

        with open(filepath, "rb") as img:
            encoded = base64.b64encode(img.read()).decode("utf-8")

        data_url = f"data:image/png;base64,{encoded}"
        out.write(f'    "{display_name}", "{data_url}",\n')

    out.write("    BLANK()\n)")
