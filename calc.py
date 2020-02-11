import os
import time
from colorama import Fore

# add individual func. to calc formulas alone(temp,density, pressure, )

# vars
Density = input("Density > ")
if Density == '':
  Density=None
else:
  Density = float(Density)

kPa = input("kPa > ")
if kPa == '':
  kPa=None
else:
  kPa = float(kPa)

Pa = input("Pa > ")
if Pa == '':
  Pa=None
else:
  Pa = float(Pa)

Lift = input("Lift > ")
if Lift == '':
  Lift=None
else:
  Lift = float(Lift)

Altitude = input('Altitude > ')
if Altitude == '':
  Altitude=None
else:
  Altitude = float(Altitude)

Drag = input("Drag > ")
if Drag == '':
  Drag=None
else:
  Drag = float(Drag)

Mass = input("Mass > ")
if Mass == '':
  Mass=None
else:
  Mass = float(Mass)

Temp = input("Temperature > ")
if Temp == '':
  Temp=None
else:
  Temp = float(Temp)

Area_of_Wings = input("Area of wings > ")
if Area_of_Wings == '':
  Area_of_Wing=None
else:
  Area_of_Wings = float(Area_of_Wings)

VelocitySqrd = input("Velocity^2(if velocity must not be squared, ignore ) > ")
if VelocitySqrd == '':
  VelocitySqrd=None
else:
  VelocitySqrd = float(pow(float(VelocitySqrd),2))

Lift_Coefficient = input("Lift Coeficient > ")
if Lift_Coefficient == '':
  Lift_Coefficient=None
else:
  Lift_Coefficient = float(Lift_Coefficient)

Drag_Coefficient = input("Drag Coefficient > ")
if Drag_Coefficient == '':
  Drag_coefficient=None
else:
  Drag_Coefficient = float(Drag_Coefficient)

print(Fore.LIGHTRED_EX + '\n  Mass Flow: \n' + Fore.RESET)

Cross_Sectional_Area = input('Cross sectional area > ')
if Cross_Sectional_Area == '':
  Cross_Sectional_Area=None
else:
  Cross_Sectional_Area = float(Cross_Sectional_Area)

Velocity = input('Velocity > ')
if Velocity == '':
  Velocity=None
else:
  Velocty = float(Velocity)

print("\n\n\n________________________________________________________\n")


def calcLiftCoefficient():

    global Mass
    global Temp
    global kPa
    global Pa
    global Density
    global Area_of_Wings
    global VelocitySqrd
    global Lift
    global Altitude

    if Lift == None:
      Lift = Mass * 9.81
      print("Lift = Mass * 9.81")
      print(Lift, " = " , Mass , " * 9.81")
      time.sleep(1.2)
      print(Fore.GREEN + "Lift = " , Lift + Fore.RESET)

    if Pa == None:
      Pa = kPa * 1000
      print("Pa = " , Pa , " * 1000")
      time.sleep(1.2)
      print(Fore.GREEN + "Pa = " , kPa + Fore.RESET)

    if Temp == None:
      Temp = 15.04 - (0.00649 * Altitude)
      print('Temp = 15.04 - 0.00649 * ', Altitude)
      time.sleep(1.5)
      print(Fore.GREEN + 'Temp =', Temp + Fore.RESET) 

    if Density == None:
      Density = kPa / 0.2869 * (Temp + 273.1)
      print(kPa , "/ 0.2869 * (" , Temp , "273.1)")
      print(Fore.GREEN + "Density = " , Density + Fore.RESET)

    DynamicPressure = 0.5 * Density * VelocitySqrd
    print("DynamicPressure = 0.5 * " , Density , " * " ,
          VelocitySqrd)
    time.sleep(1.2)
    print(Fore.CYAN + "DynamicPressure = " , DynamicPressure , "\n" + Fore.RESET)

    LiftCoefficient = 2 * Lift / DynamicPressure * Area_of_Wings * VelocitySqrd
    print("LiftCoefficient = 2 * " , Lift , " / " , DynamicPressure , " * " , Area_of_Wings , " * " , VelocitySqrd)
    time.sleep(1.2)
    print(Fore.CYAN + "LiftCoefficient = " , LiftCoefficient , Fore.RESET)


def calcLift():

  global Temp 
  global Density
  global Area_of_Wings
  global VelocitySqrd
  global kPa
  global Pa
  global Lift_Coefficient

  if kPa == None:
    kPa = Pa * 1000
    print("kPa = " + Pa + " * 1000")
    time.sleep(1.2)
    print(Fore.GREEN + "kPa = " + kPa + Fore.RESET)

  if Density == None:
    Density = kPa / 0.2869 * (Temp + 273.1)
    print(kPa + "/ 0.2869 * (" + Temp + "273.1)")
    print(Fore.GREEN + "Density = " + float(Density) + Fore.RESET)  

  Lift = Lift_Coefficient * (Density * VelocitySqrd) / 2 * Area_of_Wings 
  print("Lift = " , Lift_Coefficient , " * " , '(' , Density , ' * ' , VelocitySqrd , '/ 2) * ' , Area_of_Wings)
  print(Fore.CYAN + 'Lift = ' , Lift , Fore.RESET)


def calcDragCoefficient():
  global Temp
  global Drag 
  global Density
  global Area_of_Wings
  global VelocitySqrd
  global kPa
  global Pa
  global Altitude

  if Temp == None:
    Temp = 15.04 - (0.00649 * Altitude)
    print('15.04 - 0.00649 *', Altitude)
    time.sleep(1.5)
    print(Fore.GREEN + 'Temp =', Temp)
    print(Fore.RESET)

  if Density == None:
    Density = kPa / 0.2869 * (Temp + 273.1)
    print(kPa , "/ 0.2869 * (" , Temp , "273.1)")
    print(Fore.GREEN + "Density = " , Density)
    print(Fore.RESET)

  if kPa == None:
    kPa = Pa * 1000
    print("kPa = " , Pa , " * 1000")
    time.sleep(1.2)
    print(Fore.GREEN + "kPa = " , kPa)  
    print(Fore.RESET)

  DynamicPressure = 0.5 * Density * VelocitySqrd
  print("DynamicPressure = 0.5 * " , Density , " * " , VelocitySqrd)
  time.sleep(1.2)
  print(Fore.CYAN + "DynamicPressure = " , DynamicPressure , "\n")
  print(Fore.RESET)

  Drag_Coefficient = 2 * Drag / DynamicPressure * Area_of_Wings * VelocitySqrd
  print(Fore.CYAN + 'Drag_Coefficient = ' , Drag_Coefficient)
  print(Fore.RESET)


def calcDrag():
  global Temp 
  global Density
  global Area_of_Wings
  global VelocitySqrd
  global kPa
  global Pa
  global Drag_Coefficient

  if Temp == None:
    Temp = 15.04 - (0.00649 * Altitude)
    print('15.04 - 0.00649 *', Altitude)
    time.sleep(1.5)
    print(Fore.GREEN + 'Temp =', Temp)
    print(Fore.RESET)

  if Density == None:
    Density = kPa / 0.2869 * (Temp + 273.1)
    print(kPa , "/ 0.2869 * (" , Temp , "273.1)")
    print(Fore.GREEN + "Density = " , Density)
    print(Fore.RESET)

  if kPa == None:
    kPa = Pa * 1000
    print("kPa = " , Pa , " * 1000")
    time.sleep(1.2)
    print(Fore.GREEN + "kPa = " , kPa)
    print(Fore.RESET)

  Drag = Drag_Coefficient * (Density * VelocitySqrd) / 2 * Area_of_Wings
  print('Drag = ' , Drag_Coefficient , ' * (' , Density , ' * ' , VelocitySqrd , ' / 2) * ' , Area_of_Wings)
  print(Fore.CYAN + 'Drag = ' , Drag)
  print(Fore.RESET)


def calcMassFlow():
  global Density
  global Velocity
  global Cross_Sectional_Area
  print('[-] Not yet ready')
  perform_another_calc()


def calcMachNum():
  print('[-] Not yet ready')
  perform_another_calc()


def perform_another_calc():
  ans = input('Perform another calculation(y/n) > ')
  if ans == 'y':
    start()
  else:
    os._exit(1)


def calcReynoldNum():
  ans = input('Perform another calculation(y/n) > ')
  if ans == 'y':
    start()
  else:
    os._exit(1)


def calcSpeed_of_Sound():
  ans = input('Perform another calculation(y/n) > ')
  if ans == 'y':
    start()
  else:
    os._exit(1)


def unit_conversion():
  convert = input('convert units[y/n]?')
  if convert == 'Y'.lower():
    print('/n[1] - mi/hr > m/s\n[2] - ')
    unit = input('>')
    if unit == 1:
      mph_to_mps = VelocitySqrd / 2.237
      print(mph_to_mps)
    if unit == 2:
      pass


def individual_calc(var):
  #if int(var) == 1:
  pass


def start():
  #perform individual calcs
  #individ_calcs = input('Perform individual calculations[y/n] ?')
  #if individ_calcs == 'Y'.lower():
  #  print('\n[1] - ')
  #  var = input('> ')
  #  individual_calc(var)
  print("\n[1] - calcLiftCoefficient\n[2] - calcLift \n[3] - calcDragCoefficient\n[4] - calc Drag\n[5] - calc Mass Flow\n [6] - calc Mach #\n [7] - Reynolds #\n [8] - Speed of Sound")
  calc = input("> ")
#  try:
  if int(calc) == 1:
    calcLiftCoefficient()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 2:
    calcLift()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 3:
    calcDragCoefficient()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 4:
    calcDrag()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 5: 
    calcMassFlow()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 6:
    calcMachNum()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 7:
    calcReynoldNum()
    time.sleep(1.5)
    perform_another_calc()
  elif int(calc) == 8:
    calcSpeed_of_Sound()
    time.sleep(1.5)
    perform_another_calc()
  else:
    os._exit(1)
#  except Exception:
    #print(Fore.RED +"\n[-] Error detected...\n")
    #time.sleep(1.5)
    #print('[-] Terminating Program\n')
    #time.sleep(2)
    #print('[-] Program Terminated' + Fore.RESET)
#    os._exit(1)

start()
