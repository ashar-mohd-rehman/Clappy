Project Name : Clappy

Description : A macropad with 8 keys, volume knob and a display. Controlled by Xiao Rp2040 devboard and kmk firmware

Total Time : 

# 1 Ideation and Matrix 
I really like minecraft pvp, But switching to hotbar with scroll wheel is not very precise and loses time, 
The time lost is an advantage to your opponent, You can use the number row on your keyboard, But that is very hard for me
to reach, while moving with WASD especially with very short hands

So I decided to make this macropad which will help me in minecraft pvp and moreover I am a massive cad user, 
using macropad to pan, tilt, rotate instead of shortcuts will help me save time 

Then I went on to researching of what I can do different this time, My last macropad which I made for blueprint was
a failure because of pcb or my terrible soldering, So this time I have decided to use hotswap sockets instead of 
traditional soldered swictches

I have also decided to use the fan favourite rp2040 devboard by xiao not only because it is compact and smaller 
over the traditional pico but also because it uses the usb c and not the ancient micro usb 
<img width="778" height="703" alt="image" src="https://github.com/user-attachments/assets/95dc5bbe-47c1-43fa-a35d-7bba0bf32bbc" />

Moreover, Instead of standard tht diodes I have decided to use smd diodes specifically sod-123 for my macropad to look
even more professional 

<img width="504" height="383" alt="image" src="https://github.com/user-attachments/assets/793b6aa2-4634-465e-b099-200e0abeab38" />

Then I move onto PCB making and opened Kicad 
<img width="1328" height="805" alt="Screenshot 2026-09-29 202338" src="https://github.com/user-attachments/assets/ddf16243-b696-4def-b8d0-4944451dc74b" />

I'll be using the following libraries 

I then went and placed my matrix components and assigned global labels, Then I wired them to the xiao 
<img width="1870" height="1202" alt="Screenshot 2026-10-19 203840" src="https://github.com/user-attachments/assets/dc781bec-c65c-4013-9337-ab39b1e0530a" />

**Total Time Spent : 2h**

# 2 Finished Schematic and Assigned Footprints

So I added the rotary encoder symbol onto the sheet and added global labels to the points like A, B, and SW also Connected the Ground to GND power symbol 

I then also added a oled symbol, and did the same, That is adding global labels to the points on the symbol

Then I connected those global labels to the xiao 
<img width="1405" height="831" alt="Screenshot 2026-10-19 213204" src="https://github.com/user-attachments/assets/e7e84c0a-5027-4b97-adf1-1d876eb3a135" />

After that I ran DRC and got two errors 
 <img width="1079" height="630" alt="Screenshot 2026-10-19 213349" src="https://github.com/user-attachments/assets/b39ece0d-1fa7-43f4-8e2b-2bb9b8b74552" />

So I got confused and asked gemini about and gemini said to lowkey chill so I am gonna do that 

<img width="1352" height="257" alt="Screenshot 2026-10-19 213815" src="https://github.com/user-attachments/assets/49a78fc0-5ef1-4145-a56c-ff34fffeae10" />

After that I moved onto assigning footprints, And did that. Assigning footprints for diodes and switches were easy coz they were already their <img width="1153" height="579" alt="image" src="https://github.com/user-attachments/assets/1017abbe-42f5-4019-84aa-304aa921a8ed" />
But I couldnt find the footprints of other components like the xiao and oled

So i went onto the internet and downloaded them and then assigned them <img width="1232" height="318" alt="image" src="https://github.com/user-attachments/assets/a9cb753d-7ad4-446f-87cb-16024cef891e" />

**Total Time Spent : 1h**

# 3 Finished PCB 
So I started by marking sw1's corner as origin point 
<img width="113" height="84" alt="Screenshot 2026-10-21 173814" src="https://github.com/user-attachments/assets/ac84468e-c666-4dd7-bbae-c357ecfaea65" />
Then using position using reference tool I aligned all my switches into a grid spaced the standard 19.05 mm

But then after aliging the switches I decided to align the oled display until when I notices that it doesnt have 4 pins but many that meant it wasnt accurate to my schematic 
<img width="974" height="413" alt="Screenshot 2026-10-21 174011" src="https://github.com/user-attachments/assets/62893581-b6e9-419e-8ea1-7c0284739b2a" />
So then I went to to download the correct footprint on the internet, 
I searched and stumbled upon this website withe the footpirnt https://www.snapeda.com/parts/OLED%20128x64%201.3%22%20I2C/UNIVERSAL-SOLDER%20Electronics%20Ltd/view-part/?welcome=home

<img width="938" height="1032" alt="Screenshot 2026-10-21 174219" src="https://github.com/user-attachments/assets/dedd67bf-7e06-463e-9d25-6154582cf73b" />

So then I downloaded it and saved in ina folder called OLED.pretty because it was a .mod file which kicad doesnt accept anymore as standalone footprints
<img width="1090" height="222" alt="Screenshot 2026-10-21 174419" src="https://github.com/user-attachments/assets/9d8e5ec4-f246-42cd-b30e-64daa29a4222" />

WHICH DID NOT WORK IDK WHY BRO, I couldnt find it in assigning footprints

So then I went and opened the footprint editor I imported the .mod file and saved it into my existing Libraries which I had created earlier <img width="1158" height="637" alt="Screenshot 2026-10-21 174710" src="https://github.com/user-attachments/assets/80d9d8dc-2453-4795-a072-c04fee734cd7" />

After doing this I actually found it this time while assiging footprints 

<img width="1765" height="614" alt="Screenshot 2026-10-21 174806" src="https://github.com/user-attachments/assets/e6d06afa-ddd0-437d-a81a-f94eedbea2dc" />

So I added that yep 

But then I realised my switches were upside down which meant that the hop swap sockets would be soldered to the front and the switches would go back WHICH I OFCOURSE DIDNT want 
<img width="568" height="516" alt="Screenshot 2026-10-21 174925" src="https://github.com/user-attachments/assets/c2e2d65e-e36d-40b4-9b06-47ae2bd2a7df" />

So I Deleted all my components, and did "update pcb from schematuic" Then I flipped the switches to the backside and then places the diodes.

I then found the most optimal place for the oled and the xiao which i then aligned

After that I routed all my matrix and matrix to my xiao. Then rotary encoder to my xiao and my oled too. 

After that I created a ground pour on the bottom layer basically it lets me not route the gnd points and the entire space left on the backside becomes active gnd net so I did that 

<img width="1111" height="736" alt="Screenshot 2026-10-21 175917" src="https://github.com/user-attachments/assets/dca71d88-c219-4b70-a82b-55c10685f240" />

I then also created a pour on the first layer which wasnt connected to anything only for aesthetic reasons lol

<img width="1009" height="668" alt="Screenshot 2026-10-21 175922" src="https://github.com/user-attachments/assets/a57a826b-08d1-458c-a691-225403d36520" />

Then I ran drc and idk how but we got zero errors YIPPEEEEEEEE 

<img width="175" height="61" alt="Screenshot 2026-10-21 180038" src="https://github.com/user-attachments/assets/fcde3868-0d6c-4e44-92f2-52b57512c81e" />

and heres how my pcb looks in 3D. In the next journal Ill be adding 3d models of switches, Xiao and oled and the rotary encoder 

<img width="1179" height="715" alt="Screenshot 2026-10-21 180021" src="https://github.com/user-attachments/assets/b1ba9bf2-a856-478a-adee-2aba0694703b" />

**Total Time Spent : 1.5h**

# 4 Designed the case 

So I started by uploading models onto my pcb coz earliear it was looking  a bit naked ngl

I googled the models and downloaded them from grabcad like <img width="2252" height="1419" alt="Screenshot 2026-10-21 190640" src="https://github.com/user-attachments/assets/2582849b-fc25-4a5e-b0cf-3add6d085cfe" />

I then went into footprint editor> selected my footprint for switches and went into properties> 3d model and uploaded ts <img width="969" height="969" alt="Screenshot 2026-10-21 191238" src="https://github.com/user-attachments/assets/7527a3b2-9b22-475c-86d7-8f4c168f1459" />

I then arranged it 

<img width="502" height="533" alt="Screenshot 2026-10-21 191324" src="https://github.com/user-attachments/assets/4acfef60-0893-40be-9a58-91eab70937d3" />

But looking at 3d model of my pcb it wasnt showing idk why?
<img width="988" height="635" alt="Screenshot 2026-10-21 191505" src="https://github.com/user-attachments/assets/c885049d-cfea-4271-9d85-2fda31036d3b" />

So I decided to add 3d models one by one onto the footprints on my pcb one by one <img width="1165" height="794" alt="Screenshot 2026-10-21 192001" src="https://github.com/user-attachments/assets/3f8c32ad-74f6-4ce1-a7fb-5e3836ddb7de" />
<img width="1177" height="896" alt="Screenshot 2026-10-21 192226" src="https://github.com/user-attachments/assets/44eaefc4-5111-4a09-93d9-34673a5fbd1c" />

I was doing good until I realized I had made a grave mistake, I embedded the switches in too deep 
so This was how it was supposed to look <img width="780" height="635" alt="Screenshot 2026-10-21 192332" src="https://github.com/user-attachments/assets/dd7bdf50-ed32-46ef-a223-18223761b7d3" />

This lead to a huge height difference <img width="1069" height="446" alt="Screenshot 2026-10-21 192344" src="https://github.com/user-attachments/assets/0282fe3f-cf68-41e4-b6cd-f58961c66675" />

So i went back and fixed each one of em <img width="1506" height="836" alt="Screenshot 2026-10-21 192619" src="https://github.com/user-attachments/assets/0249d7a2-9126-48ef-ba77-b64f69324bcb" />

Then I added the rotary encoder model <img width="1281" height="981" alt="Screenshot 2026-10-21 192642" src="https://github.com/user-attachments/assets/60ed21b7-7ea7-4864-b3a9-19cb1de3e854" />
and arranged it 

<img width="999" height="616" alt="Screenshot 2026-10-21 192740" src="https://github.com/user-attachments/assets/90ecaba2-19f5-49d6-9ced-c86eb3c23401" />

And then the oled display <img width="1237" height="766" alt="Screenshot 2026-10-21 192925" src="https://github.com/user-attachments/assets/1333189d-4b83-4f74-88d8-529f1523a1fa" />

I then added mounting holes onto my pcb <img width="1438" height="871" alt="Screenshot 2026-10-21 193318" src="https://github.com/user-attachments/assets/367e155f-f305-4a0e-ba0d-280f0012af20" />

And heres how my final pcb be lookin <img width="1188" height="733" alt="Screenshot 2026-10-21 193333" src="https://github.com/user-attachments/assets/eed3cba3-5605-4932-9203-a20e07fdf940" />

then I uploaded the pcb model onto my fusion360 <img width="1715" height="817" alt="Screenshot 2026-10-23 173336" src="https://github.com/user-attachments/assets/6ed99758-4d65-402c-aa59-f7eb28fd91ae" />

after that I started creating my case and created the bottom case lol <img width="2149" height="1111" alt="Screenshot 2026-10-23 173235" src="https://github.com/user-attachments/assets/27b9366f-fbe4-4c16-92b2-b828f8f4b771" />

Then I started making the top case by making holes for my components and all. 
<img width="1442" height="929" alt="Screenshot 2026-10-23 173843" src="https://github.com/user-attachments/assets/1c4427af-35e0-42e0-84d2-fd5e65deb59a" />


I the used rectangular pattern to duplicate the switch holes but realised that it couldnt be done for the bottom row as it has a rotary encoder hole already so i had to seperate my rectangular patter into  3 parts lol <img width="1277" height="822" alt="Screenshot 2026-10-23 174229" src="https://github.com/user-attachments/assets/986e3beb-4ea6-41b7-a4f4-a947e4b74cb1" />

after the case was done I started renderin <img width="1431" height="768" alt="Screenshot 2026-10-23 175338" src="https://github.com/user-attachments/assets/45a2f3e4-db36-40af-8105-ada8d1e381d5" />

case photo <img width="1655" height="988" alt="Screenshot 2026-10-23 175459" src="https://github.com/user-attachments/assets/ed88f537-b247-4e08-8400-d7a1d4d88ddd" />

**Total Time Spent: 2h**
