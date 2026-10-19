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
