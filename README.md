# final-project-prices

## Objectives

  1. Access the Bureau of Labor Statistics data
  2. Create a tool to facilitate downloading this economic data
  3. Generate and quickly display the data downloaded in different formats (level, monthly changes and yearly changes)

## Instructions to run the program

> Useful links:
>   + [Accessing the Public Data API with Python](https://www.bls.gov/developers/api_python.htm)
>   + [BLS Public Data API Signatures]([/exercises/groceries/README.md](https://www.bls.gov/developers/api_signature_v2.htm#all))
>   + [BLS Frequently Asked Questions (FAQs)](https://www.bls.gov/developers/api_FAQs.htm#signatures3)
>   + [BLS Series ID Formats](https://www.bls.gov/help/hlpforma.htm#CU)

### Repo Setup

### Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n prices-env python=3.7 # (first time only)
conda activate prices-env
```

Make sure you have installed all packages:

```sh

pip install requests
pip install dotenv
pip install pandas
pip install matplotlib

```

## API Setup

The provided code includes a variable called `products` which facilitates management of the products inventory from within the application's source code.

If you'd like to manage the products inventory via a CSV file instead, download the provided ["products.csv"](/data/products.csv) file and place it into your project directory in a directory called "data". And you can later try to reference that data instead of the provided `products` variable.

If you'd like to manage the products inventory via Google Sheet document instead, reference this provided [products sheet](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit?usp=sharing). And you can later try to reference that data instead of the provided `products` variable. See the "Integrating with a Google Sheets Datastore" challenge for more info.

## Run the program

From within the virtual environment, run the Python script from the command-line:

```sh
python inflation_new.py
```

## Example Output

``` sh
        Code                Name
0       AA0                 All items - old base
1       AA0R                Purchasing power of the consumer dollar - old base
2       SA0                 All items
3       SA0E                Energy
4       SA0L1               All items less food
5       SA0L12              All items less food and shelter
6       SA0L12E             All items less food, shelter, and energy
7       SA0L12E4            All items less food, shelter, energy, and used cars and trucks
8       SA0L1E              All items less food and energy
9       SA0L2               All items less shelter
10      SA0L5               All items  less medical care
11      SA0LE               All items less energy
12      SA0R                Purchasing power of the consumer dollar
13      SA311               Apparel less footwear
14      SAA                 Apparel
15      SAA1                Mens and boys apparel
16      SAA2                Womens and girls apparel
17      SAC                 Commodities
18      SACE                Energy commodities
19      SACL1               Commodities less food
20      SACL11              Commodities less food and beverages
21      SACL1E              Commodities less food and energy commodities
22      SACL1E4             Commodities less food, energy, and used cars and trucks
23      SAD                 Durables
24      SAE                 Education and communication
25      SAE1                Education
26      SAE2                Communication
27      SAE21               Information and information processing
28      SAEC                Education and communication commodities
29      SAES                Education and communication services
30      SAF                 Food and beverages
31      SAF1                Food
32      SAF11               Food at home
33      SAF111              Cereals and bakery products
34      SAF112              Meats, poultry, fish, and eggs
35      SAF1121             Meats, poultry, and fish
36      SAF11211            Meats
37      SAF113              Fruits and vegetables
38      SAF1131             Fresh fruits and vegetables
39      SAF114              Nonalcoholic beverages and beverage materials
40      SAF115              Other food at home
41      SAF116              Alcoholic beverages
42      SAG                 Other goods and services
43      SAG1                Personal care
44      SAGC                Other goods
45      SAGS                Other personal services
46      SAH                 Housing
47      SAH1                Shelter
48      SAH2                Fuels and utilities
49      SAH21               Household energy
50      SAH3                Household furnishings and operations
51      SAH31               Household furnishings and supplies
52      SAM                 Medical care
53      SAM1                Medical care commodities
54      SAM2                Medical care services
55      SAN                 Nondurables
56      SAN1D               Domestically produced farm food
57      SANL1               Nondurables less food
58      SANL11              Nondurables less food and beverages
59      SANL113             Nondurables less food, beverages, and apparel
60      SANL13              Nondurables less food and apparel
61      SAR                 Recreation
62      SARC                Recreation commodities
63      SARS                Recreation services
64      SAS                 Services
65      SAS24               Utilities and public transportation
66      SAS2RS              Rent of shelter
67      SAS367              Other services
68      SAS4                Transportation services
69      SASL2RS             Services less rent of shelter
70      SASL5               Services less medical care services
71      SASLE               Services less energy services
72      SAT                 Transportation
73      SAT1                Private transportation
74      SATCLTB             Transportation commodities less motor fuel
75      SEAA                Mens apparel
76      SEAA01              Mens suits, sport coats, and outerwear
77      SEAA02              Mens underwear, nightwear, swimwear and accessories
78      SEAA03              Mens shirts and sweaters
79      SEAA04              Mens pants and shorts
80      SEAB                Boys apparel
81      SEAC                Womens apparel
82      SEAC01              Womens outerwear
83      SEAC02              Womens dresses
84      SEAC03              Womens suits and separates
85      SEAC04              Womens underwear, nightwear, swimwear and accessories
86      SEAD                Girls apparel
87      SEAE                Footwear
88      SEAE01              Mens footwear
89      SEAE02              Boys and girls footwear
90      SEAE03              Womens footwear
91      SEAF                Infants and toddlers apparel
92      SEAG                Jewelry and watches
93      SEAG01              Watches
94      SEAG02              Jewelry
95      SEEA                Educational books and supplies
96      SEEB                Tuition, other school fees, and childcare
97      SEEB01              College tuition and fees
98      SEEB02              Elementary and high school tuition and fees
99      SEEB03              Child care and nursery school
100     SEEB04              Technical and business school tuition and fees
101     SEEC                Postage and delivery services
102     SEEC01              Postage
103     SEEC02              Delivery services
104     SEED                Telephone services
105     SEED03              Wireless telephone services
106     SEED04              Land-line telephone services
107     SEEE                Information technology, hardware and services
108     SEEE01              Computers, peripherals, and smart home assistant devices
109     SEEE02              Computer software and accessories
110     SEEE03              Internet services and electronic information providers
111     SEEE04              Telephone hardware, calculators, and other consumer information items
112     SEEEC               Information technology commodities
113     SEFA                Cereals and cereal products
114     SEFA01              Flour and prepared flour mixes
115     SEFA02              Breakfast cereal
116     SEFA03              Rice, pasta, cornmeal
117     SEFB                Bakery products
118     SEFB01              Bread
119     SEFB02              Fresh biscuits, rolls, muffins
120     SEFB03              Cakes, cupcakes, and cookies
121     SEFB04              Other bakery products
122     SEFC                Beef and veal
123     SEFC01              Uncooked ground beef
124     SEFC02              Uncooked beef roasts
125     SEFC03              Uncooked beef steaks
126     SEFC04              Uncooked other beef and veal
127     SEFD                Pork
128     SEFD01              Bacon, breakfast sausage, and related products
129     SEFD02              Ham
130     SEFD03              Pork chops
131     SEFD04              Other pork including roasts, steaks, and ribs
132     SEFE                Other meats
133     SEFF                Poultry
134     SEFF01              Chicken
135     SEFF02              Other uncooked poultry including turkey
136     SEFG                Fish and seafood
137     SEFG01              Fresh fish and seafood
138     SEFG02              Processed fish and seafood
139     SEFH                Eggs
140     SEFJ                Dairy and related products
141     SEFJ01              Milk
142     SEFJ02              Cheese and related products
143     SEFJ03              Ice cream and related products
144     SEFJ04              Other dairy and related products
145     SEFK                Fresh fruits
146     SEFK01              Apples
147     SEFK02              Bananas
148     SEFK03              Citrus fruits
149     SEFK04              Other fresh fruits
150     SEFL                Fresh vegetables
151     SEFL01              Potatoes
152     SEFL02              Lettuce
153     SEFL03              Tomatoes
154     SEFL04              Other fresh vegetables
155     SEFM                Processed fruits and vegetables
156     SEFM01              Canned fruits and vegetables
157     SEFM02              Frozen fruits and vegetables
158     SEFM03              Other processed fruits and vegetables including dried
159     SEFN                Juices and nonalcoholic drinks
160     SEFN01              Carbonated drinks
161     SEFN02              Frozen noncarbonated juices and drinks
162     SEFN03              Nonfrozen noncarbonated juices and drinks
163     SEFP                Beverage materials including coffee and tea
164     SEFP01              Coffee
165     SEFP02              Other beverage materials including tea
166     SEFR                Sugar and sweets
167     SEFR01              Sugar and sugar substitutes
168     SEFR02              Candy and chewing gum
169     SEFR03              Other sweets
170     SEFS                Fats and oils
171     SEFS01              Butter and margarine
172     SEFS02              Salad dressing
173     SEFS03              Other fats and oils including peanut butter
174     SEFT                Other foods
175     SEFT01              Soups
176     SEFT02              Frozen and freeze dried prepared foods
177     SEFT03              Snacks
178     SEFT04              Spices, seasonings, condiments, sauces
179     SEFT05              Baby food
180     SEFT06              Other miscellaneous foods
181     SEFV                Food away from home
182     SEFV01              Full service meals and snacks
183     SEFV02              Limited service meals and snacks
184     SEFV03              Food at employee sites and schools
185     SEFV04              Food from vending machines and mobile vendors
186     SEFV05              Other food away from home
187     SEFW                Alcoholic beverages at home
188     SEFW01              Beer, ale, and other malt beverages at home
189     SEFW02              Distilled spirits at home
190     SEFW03              Wine at home
191     SEFX                Alcoholic beverages away from home
192     SEGA                Tobacco and smoking products
193     SEGA01              Cigarettes
194     SEGA02              Tobacco products other than cigarettes
195     SEGB                Personal care products
196     SEGB01              Hair, dental, shaving, and miscellaneous personal care products
197     SEGB02              Cosmetics, perfume, bath, nail preparations and implements
198     SEGC                Personal care services
199     SEGC01              Haircuts and other personal care services
200     SEGD                Miscellaneous personal services
201     SEGD01              Legal services
202     SEGD02              Funeral expenses
203     SEGD03              Laundry and dry cleaning services
204     SEGD04              Apparel services other than laundry and dry cleaning
205     SEGD05              Financial services
206     SEGE                Miscellaneous personal goods
207     SEHA                Rent of primary residence
208     SEHB                Lodging away from home
209     SEHB01              Housing at school, excluding board
210     SEHB02              Other lodging away from home including hotels and motels
211     SEHC                Owners equivalent rent of residences
212     SEHC01              Owners equivalent rent of primary residence
213     SEHD                Tenants and household insurance
214     SEHE                Fuel oil and other fuels
215     SEHE01              Fuel oil
216     SEHE02              Propane, kerosene, and firewood
217     SEHF                Energy services
218     SEHF01              Electricity
219     SEHF02              Utility (piped) gas service
220     SEHG                Water and sewer and trash collection services
221     SEHG01              Water and sewerage maintenance
222     SEHG02              Garbage and trash collection
223     SEHH                Window and floor coverings and other linens
224     SEHH01              Floor coverings
225     SEHH02              Window coverings
226     SEHH03              Other linens
227     SEHJ                Furniture and bedding
228     SEHJ01              Bedroom furniture
229     SEHJ02              Living room, kitchen, and dining room furniture
230     SEHJ03              Other furniture
231     SEHK                Appliances
232     SEHK01              Major appliances
233     SEHK02              Other appliances
234     SEHL                Other household equipment and furnishings
235     SEHL01              Clocks, lamps, and decorator items
236     SEHL02              Indoor plants and flowers
237     SEHL03              Dishes and flatware
238     SEHL04              Nonelectric cookware and tableware
239     SEHM                Tools, hardware, outdoor equipment and supplies
240     SEHM01              Tools, hardware and supplies
241     SEHM02              Outdoor equipment and supplies
242     SEHN                Housekeeping supplies
243     SEHN01              Household cleaning products
244     SEHN02              Household paper products
245     SEHN03              Miscellaneous household products
246     SEHP                Household operations
247     SEHP01              Domestic services
248     SEHP02              Gardening and lawncare services
249     SEHP03              Moving, storage, freight expense
250     SEHP04              Repair of household items
251     SEMC                Professional services
252     SEMC01              Physicians services
253     SEMC02              Dental services
254     SEMC03              Eyeglasses and eye care
255     SEMC04              Services by other medical professionals
256     SEMD                Hospital and related services
257     SEMD01              Hospital services
258     SEMD02              Nursing homes and adult day services
259     SEMD03              Care of invalids and elderly at home
260     SEME                Health insurance
261     SEMF                Medicinal drugs
262     SEMF01              Prescription drugs
263     SEMF02              Nonprescription drugs
264     SEMG                Medical equipment and supplies
265     SERA                Video and audio
266     SERA01              Televisions
267     SERA02              Cable and satellite television service
268     SERA03              Other video equipment
269     SERA04              Video discs and other media, including rental of video
270     SERA05              Audio equipment
271     SERA06              Recorded music and music subscriptions
272     SERAC               Video and audio products
273     SERAS               Video and audio services
274     SERB                Pets, pet products and services
275     SERB01              Pets and pet products
276     SERB02              Pet services including veterinary
277     SERC                Sporting goods
278     SERC01              Sports vehicles including bicycles
279     SERC02              Sports equipment
280     SERD                Photography
281     SERD01              Photographic equipment and supplies
282     SERD02              Photographers and photo processing
283     SERE                Other recreational goods
284     SERE01              Toys
285     SERE02              Sewing machines, fabric and supplies
286     SERE03              Music instruments and accessories
287     SERF                Other recreation services
288     SERF01              Club membership for shopping clubs, fraternal, or other organizations, or
participant sports fees
289     SERF02              Admissions
290     SERF03              Fees for lessons or instructions
291     SERG                Recreational reading materials
292     SERG01              Newspapers and magazines
293     SERG02              Recreational books
294     SETA                New and used motor vehicles
295     SETA01              New vehicles
296     SETA02              Used cars and trucks
297     SETA03              Leased cars and trucks
298     SETA04              Car and truck rental
299     SETB                Motor fuel
300     SETB01              Gasoline (all types)
301     SETB02              Other motor fuels
302     SETC                Motor vehicle parts and equipment
303     SETC01              Tires
304     SETC02              Vehicle accessories other than tires
305     SETD                Motor vehicle maintenance and repair
306     SETD01              Motor vehicle body work
307     SETD02              Motor vehicle maintenance and servicing
308     SETD03              Motor vehicle repair
309     SETE                Motor vehicle insurance
310     SETF                Motor vehicle fees
311     SETF01              State motor vehicle registration and license fees
312     SETF03              Parking and other fees
313     SETG                Public transportation
314     SETG01              Airline fares
315     SETG02              Other intercity transportation
316     SETG03              Intracity transportation
317     SS01031             Rice
318     SS02011             White bread
319     SS02021             Bread other than white
320     SS02041             Fresh cakes and cupcakes
321     SS02042             Cookies
322     SS02063             Fresh sweetrolls, coffeecakes, doughnuts
323     SS0206A             Crackers, bread, and cracker products
324     SS0206B             Frozen and refrigerated bakery products, pies, tarts, turnovers
325     SS04011             Bacon and related products
326     SS04012             Breakfast sausage and related products
327     SS04031             Ham, excluding canned
328     SS05011             Frankfurters
329     SS05014             Lamb and organ meats
330     SS05015             Lamb and mutton
331     SS0501A             Lunchmeats
332     SS06011             Fresh whole chicken
333     SS06021             Fresh and frozen chicken parts
334     SS07011             Shelf stable fish and seafood
335     SS07021             Frozen fish and seafood
336     SS09011             Fresh whole milk
337     SS09021             Fresh milk other than whole
338     SS10011             Butter
339     SS11031             Oranges, including tangerines
340     SS13031             Canned fruits
341     SS14011             Frozen vegetables
342     SS14021             Canned vegetables
343     SS14022             Dried beans, peas, and lentils
344     SS16011             Margarine
345     SS16014             Peanut butter
346     SS17031             Roasted coffee
347     SS17032             Instant coffee
348     SS18041             Salt and other seasonings and spices
349     SS18042             Olives, pickles, relishes
350     SS18043             Sauces and gravies
351     SS1804B             Other condiments
352     SS18064             Prepared salads
353     SS20021             Whiskey at home
354     SS20022             Distilled spirits, excluding whiskey, at home
355     SS20051             Beer, ale, and other malt beverages away from home
356     SS20052             Wine away from home
357     SS20053             Distilled spirits away from home
358     SS27051             Land-line interstate toll calls
359     SS27061             Land-line intrastate toll calls
360     SS30021             Laundry equipment
361     SS31022             Video discs and other media
362     SS31023             Video game hardware, software and accessories
363     SS33032             Stationery, stationery supplies, gift wrap
364     SS45011             New cars
365     SS4501A             New cars and trucks
366     SS45021             New trucks
367     SS45031             New motorcycles
368     SS47014             Gasoline, unleaded regular
369     SS47015             Gasoline, unleaded midgrade
370     SS47016             Gasoline, unleaded premium
371     SS47021             Motor oil, coolant, and fluids
372     SS48021             Vehicle parts and equipment other than tires
373     SS52051             Parking fees and tolls
374     SS53021             Intercity bus fare
375     SS53022             Intercity train fare
376     SS53023             Ship fare
377     SS53031             Intracity mass transit
378     SS5702              Inpatient hospital services
379     SS5703              Outpatient hospital services
380     SS61011             Toys, games, hobbies and playground equipment
381     SS61021             Film and photographic supplies
382     SS61023             Photographic equipment
383     SS61031             Pet food
384     SS61032             Purchase of pets, pet supplies, accessories
385     SS62011             Automobile service clubs
386     SS62031             Admission to movies, theaters, and concerts
387     SS62032             Admission to sporting events
388     SS62051             Photographer fees
389     SS62052             Photo Processing
390     SS62053             Pet services
391     SS62054             Veterinarian services
392     SS62055             Rental of video discs and other media
393     SS68021             Checking account and other bank services
394     SS68023             Tax return preparation and other accounting fees
395     SSEA011             College textbooks
396     SSFV031A            Food at elementary and secondary schools
397     SSGE013             Infants equipment
398     SSHJ031             Infants furniture
---------------------------------------------------------
PLEASE CHOOSE THE CODE OF THE ITEMS IN THE LIST ABOVE
Example: SSHJ031 (for Infants furniture)
---------------------------------------------------------
Please input code: AA0
Please input initial year (Example: 2000): 2000
Please input final year (Example: 2019): 2019
Please input transformation (Original, MoM, YoY): YoY

```


#################################

