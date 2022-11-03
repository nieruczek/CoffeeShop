# CoffeeShop
Simplified control system for Menue and Customers' discounts.

For correct work all the files should be input to the same folder.

```mermaid

flowchart TB
  id1[PROGRAM STARTS: What's the option?]
  id1-->id2[Add new item to the Menue]
  id1-->id3[Delete item]
  id1-->id4[New customer]
  id1-->id5[Regular customer]
  id1-->id6[Nothig]
  id2-->id7[You can create new Menue item and set its price]
  id3-->id8[The selected one is deleted forever]
  id4-->id9[New customer gets his/her unique number]
  id9-->id10[System asks about the customer's card balance. Default currency is PLN]
  id10-->id11[System asks the actual currency for buying]
  id11-->id12[The Menue is opened. The customer can choose a few items]
  id12-->id13[The customers sees the sum to pay in actual currency]
  id13-->id14[The customer sees the sum to pay in default currency]
  id14-->id15[The customer sees his/her card balance in default currency]  
  id5-->id16[System asks about the customer's card balance. Default currency is PLN]
  id16-->id17[System asks about the customer's individual number]
  id17-->id18[System asks about actual currency for buying]
  id18-->id19[The Menue is opened. The customer can choose a few items]
  id19-->id20[The customers sees the sum to pay in actual currency]
  id20-->id21[The customer sees the sum to pay in default currency]
  id21-->id22[The system checks if there should be any discount]
  id22-->id23[There is no discount]
  id23-->id24[The customer sees his/her card balance in default currency]  
  id22-->id25[There is discount]
  id25-->id26[Message about discount]
  id26-->id27[Message about final sum to pay]
  id27-->id28[The customer sees his/her card balance in default currency] 
```
#### TO CHANGE THE MENUE ITEM'S PRICE
First delete the Menue item. Then create it again with a new price
