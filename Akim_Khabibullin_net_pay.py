#Assignment: Net pay calculator 
#Class: DEV 108
#Date: 4/14/25
#Author: Akim Khabibullin
#Description: Program to calculate the net pay given hours worked,
#hourly rate and tax withholding percent

#get user info
print("Welcome to Net Pay Calculator");
name = input("Your Name: ");
hours = int(input("Hours Woked: "));
rate = int(input("Hourly pay Rate: "));
tax = float(input("Tax Withholding: "));
#make the pay amounts
grosspay = hours * rate;
netpay = grosspay - (grosspay * (tax / 100));

#display results
print("Hello" + name);
print("Your Gross Pay: $" + str(grosspay));
print("Your Net Pay: $" + str(netpay));
print("good Bye!");
