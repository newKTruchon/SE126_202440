import random

def printHand():
  print("\nYour Hand:")
  for i in range(0, len(playerHand)):
    print(f"\t{masterNames[playerHand[i]]}{masterSuit[playerHand[i]]}")

def printDealerHand():
  print("\nDealer Hand:")
  for i in range(0, len(dealerHand)):
    print(f"\t{masterNames[dealerHand[i]]}{masterSuit[dealerHand[i]]}")

def playerValueCheck(hand, val):
  #determine player hand value
  pValue = 0
  for i in range(0, len(hand)):
    if val[hand[i]] != 1:
      pValue += val[hand[i]]
    else:
      if val[hand[i]] <= 10:
        pValue += 11
      else:
        pValue += 1
  return pValue
    
#initialize blank lists
masterDeck = []
masterSuit = []
masterValue = []
masterNames = []
playerHand = []
dealerHand = []
drawCount = 0
dealerValue = 0
playerValue = 0
blackJack = False
dealerControl = 0
aceControl = 0
daceControl = 0
pAcePosition = []
dAcePosition = []

#populate deck list
for i in range(0,52):
  masterDeck.append(i+1)

random.shuffle(masterDeck) #shuffle deck

for i in range(0,52):
  if masterDeck[i] % 4 == 0:
    masterSuit.append("Hearts")
  elif masterDeck[i] % 4 == 1:
    masterSuit.append("Diamonds")
  elif masterDeck[i] % 4 == 2:
    masterSuit.append("Spades")
  elif masterDeck[i] % 4 == 3:
    masterSuit.append("Clubs")

  masterValue.append(masterDeck[i] // 4)
  
  if masterValue[i] == 1:
    masterNames.append("Ace of ")
  elif masterValue[i] == 11:
    masterValue[i] = 10
    masterNames.append("Jack of ")
  elif masterValue[i] == 12:
    masterValue[i] = 10
    masterNames.append("Queen of ")
  elif masterValue[i] == 11:
    masterValue[i] = 10
    masterNames.append("King of ")
  else:
    for j in range(2,11):
      if masterValue[i] == j:
        tempName = str(j) + " of "
        masterNames.append(tempName)

#draw 2 cards for player
playerHand.append(drawCount)
drawCount += 1
playerHand.append(drawCount)
drawCount += 1
#draw 2 cards for dealer
dealerHand.append(drawCount)
drawCount += 1
dealerHand.append(drawCount)
drawCount += 1

printHand()
print("\nDealer face card:")
print(f"\t{masterNames[2]}{masterSuit[2]}")

if masterValue[0] == 1 and masterValue[1] == 10 or masterValue[1] == 1 and masterValue[0] == 10:
  print("Blackjack! you win 1.5x payout!")
  blackJack = True
if blackJack == False:
  playerChoice = input("\n\tHit: 'H'\n\tStand: 'S'\n\tWhat would you like to do?: ")
  while playerChoice.lower() == "h":
    playerHand.append(drawCount)
    drawCount += 1
    print(f"Your card: {masterNames[playerHand[-1]]}{masterSuit[playerHand[-1]]}")
    playerValue = playerValueCheck(playerHand, masterValue)
    if playerValue > 21:
      for i in range(0, len(playerHand)):
        if masterNames[playerHand[i]] == "Ace of ":
          aceControl = 1
          pAcePosition.append(i)
      if aceControl == 1:
        for i in range(0, len(pAcePosition)):
          playerValue = playerValueCheck(playerHand, masterValue)
          if playerValue > 21:
            masterValue[pAcePosition[i]] -= 10
        playerValue = playerValueCheck(playerHand, masterValue)
      else:
        print("\nBust! You lost :(\n")
        playerChoice = "s"
        dealerControl = -1
    if dealerControl != -1:
      if dealerValue == 21 and len(dealerHand) == 2 and blackJack == False:
        print("\nDealer Blackjack! you lose :(")
      else:
        playerChoice = input("\n\tHit: 'H'\n\tStand: 'S'\n\tWhat would you like to do?: ")
  if playerChoice.lower() == "s":
    while dealerControl == 0:
      for i in range(0, len(dealerHand)):
        if masterValue[dealerHand[i]] != 1:
          dealerValue += masterValue[dealerHand[i]]
        else:
          if masterValue[dealerHand[i]] <= 10:
            dealerValue += 11
          else:
            dealerValue += 1
      dealerValue = playerValueCheck(dealerHand, masterValue)
      if dealerValue > 21:
        for i in range(0, len(dealerHand)):
          if masterNames[dealerHand[i]] == "Ace of ":
            daceControl = 1
            dAcePosition.append(i)
        dealerControl = 2
      if daceControl == 1:
        for i in range(0, len(dAcePosition)):
          dealerValue = playerValueCheck(dealerHand, masterValue)
          if dealerValue > 21:
            masterValue[dAcePosition[i]] -= 10
        dealerValue = playerValueCheck(dealerHand, masterValue)
      elif dealerValue <= 15:
        dealerHand.append(drawCount)
        drawCount += 1
      else:
        dealerControl = 1
    #determine player hand value
    playerValue = playerValueCheck(playerHand, masterValue)
    #print final values
    printHand()
    printDealerHand()
    #determine final outcome
    if dealerControl == 1 or dealerControl == 0:
      if playerValue < dealerValue:
        print("\nYou lose :(")
      elif playerValue == dealerValue:
        print("\nStandoff!")
      else:
        print("\nYou won!")
    elif dealerControl == 2:
      print("\nDealer Bust! You won!")