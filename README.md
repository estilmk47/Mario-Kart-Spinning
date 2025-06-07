# Mario Kart Spinning
This is an open source Mario Kart project that provides an alternative hardware setup that can use the toy-con controller method in Mario Kart 8 Delux on the Nintendo Switch to play the game and control the kart in game.
The project is heavely inpired by the cardboard Steeringwheel and Pedal in the Toy-Con Vehicle kit, but redesigned from scrath to be (relatively) easy to construct. The "IR Image" in that the Right-Joycon controller is "watching" is "static" and estimated based on publically available information. A generic "race car steering wheel" and a "gas pedal" was designed in blender and is converted to .dxf format to be easily laser cut. Additionally the project consist of a sofware package meant to be deployed on a RaspberryPi that connects to, up to 4 *bikes*-*Left Joycon* pair.

# Requirements
## Steering wheel and Pedal
- Laser Cutter (that can cut 3mm sheets) [.dxf]
- 3D Printer (that can print the .stl files) [.stl]
## Aditional 
- 8x 20mm m4 bolts
- 5x 10mm m4 bolts
- 13x (standard) m4 nuts
    Alternatively (depending on how permanet of a solution you want) up to:
    - 7x fastening nuts
    - 6x wingnuts
- Wood Glue
- 2x Rubber Bands ("small"-ish ones)
- 1x Graffite Pencil (The wider the graffite core, the better)
## Spinning
- Laser Cutter (that can cut 3mm sheets) [.dxf]
- 3D Printer (that can print the .stl files) [.stl]
- RaspebryPi (that will run the server script) [.py]
    - Power suply, mini-HDMI cable, Monitor and Keyboard & Mouse 
    - Additional jumper cables for the GPIO and servo motors
- Servo motor (up to 4 -> one for each bike/controller)

# HOW 2
If you want to do any personlaizations to files, feel free to edit the software and the rest of the project files (hint: open and modify the <name_of_component>_model.blend file). If you want to share your improvements with the rest of us, be suire to fork the project clean your contribution and request a merge on github. 😊

## Steering Wheel and Pedal
The complete Steering and Pedal set:
(The .dxf file is optimized to be cut on a "aa"x"aa"x"3" (mm)^2 ["l"x"b"x"h"] sheet of MDF)

Cut the files in the 'HARDWARE'>'output'>'LASER_CUT'>'BULK_CUT':
1. STEERING_WHEEL_CMPLT.dxf -> Steering wheel CMPLT
2. PEDAL_CMPLT_01.dxf -> Pedal Part **1** out of **1**
3. PEDAL_CMPLT_02.dxf -> Pedal Part **2** out of **2**
4. PEDAL_CMPLT_03.dxf -> Pedal Part **3** out of **3**
5. PEDAL_CMPLT_04.dxf -> Pedal Part **3** out of **3**


**Hint**: if you order them like this:

######################################
####### SW ############## PDL_03 #####
######################### PDL_04 #####
####### PDL_01 ## PD_02 ##############
######################################

They fit snuggly on one sheet. 
**Another hint**: If the bed you are cutting on is not super-duper-flat, you might want to cut the parts in smaller bulk sizes and "calibrate" the laser in-between, alternatively move the sheet and keep the origin of the laser close to its calibration point. This differs from laser cutter to laser cutter and might not be applicable to yours.

**Another another hint**: Remember to hold on to (most) of the small parts as well you will probably need them. For the very smallest components a few extra /spares are included in the "white space" of the cut file so that when your clumby hands and eyes innevitably lose some of them no worries you have a few extra. The smallest parts can also be cut seperatly: look for the CH.dxg file ('CH': Choking Hazards). 


## For a single components:
0. (Download the requirements for the project [you will need a python version that match (roughly) the same python version as your blender version]):
    0. Download VS code, Blender and install Python
    1. Open the folder that the .blend project is located in your IDE (VS code)
    2. In the terminal write: python -m venv .venv to create a viritual environment to download this projects dependencies (It is imperative that the folder is called '.venv' and is located in this folder unless you intend to edit the venv path variable in the blend_2_dxf.py script)
    3. Download and install the dependancies:
        0. .venv/Script/activate [on Windows]
        1. pip install ezdxf
 
1. Open the corresponding <NAME_OF_COMPONENT>_CUT.blend file.
    1. (and a third) In the *Scripting* window in the *Header Bar* (very top horizontal tool bar of the blender window. Consists of: File, Edit, Render, Window, etc ) inside blender open a new script and select the blend_2_dxf.py script. 
    1. (and two thirds) Enable the console by clicking *Window* > *Toggle System Console* in the *Header Bar* 
2. Copy the name of the component you want the .dxf file of and paste it in the obj_name variable (very bottom of the blend_2_dxf.py script under the if \__name__ == '\__main__' statement). Run the script: Play button in the *Text Editor* - *Area* in the *Scripting* window.
3. View your file in the 'output' folder.

## Spinning 
TODO