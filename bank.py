#Accessing the Locker
username=input('Username: ').strip()
coin=0.0
file_list=list()
try:
  with open('lockers.txt','r') as file:
      for line in file:
         file_list.append(line)
         part=line.split(':')
         if part[0].strip() == username:
           coin=float(part[1].strip())
except:
  print('starting brand new')

#Transaction
def withdraw(wit):
  if coin < float(wit):
      print(f'you have {coin:.2f}  insufficient funds!')
      return 0.0
  return float(wit)
need=input('Deposit or Withdraw (d/w)?').strip().lower()
deposit=0.0
withdr=0.0
if need == 'd':
  try: 
    deposit=input('Amount you want to deposit: ')
    coin+=float(deposit)
    print(f'your coin  balance is now {coin:.2f}')
  except ValueError:
    print("invalid input, number only!")
    quit()
elif need == 'w':
  try:
     withdraw_input=input('Amount you want to withdraw: ')
     withdr=withdraw(withdraw_input)
     if withdr > 0.0: 
        coin-=withdr
        print(f'You withdraw {withdr:.2f}. Balance is  now {coin:.2f}')
  except ValueError:
     print('Invalid input, numbers only!')
     quit()
#update the user 
update_existing_user=False
with open('lockers.txt','w') as file:
  for line  in file_list:
     data=line.split(':')
     if line.startswith(f'{username}:'):
        file.write(f'{username}: {coin:.2f}\n')
        update_existing_user=True
     else:
        if data[0].strip() != username:
            file.write(line)
  if not update_existing_user:
     file.write(f'{username}: {coin:.2f}\n') 
with open('bank_log.txt','a') as file2:
  file2.write(f'User: {username} | Action: {'deposit' if need == 'd' else 'withdraw'} | Amount: {deposit if  need == 'd' else withdr} | Total: {coin:.2f}\n')
