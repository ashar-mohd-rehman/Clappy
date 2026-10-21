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

#2 Finished Schematic and Assigned Footprints

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
