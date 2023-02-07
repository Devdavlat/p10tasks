# Currency Converter App

## check currency 
![Screenshot from 2023-02-07 23-41-49](https://user-images.githubusercontent.com/109902921/217337324-8d56e3c6-c720-45e1-804d-b64446359957.png)

![Screenshot from 2023-02-07 23-39-17](https://user-images.githubusercontent.com/109902921/217337335-70df2bc6-bf31-42b3-a544-cfbb9106099a.png)

## Refrehs data 
### (har safar conventer ishlaganda api ishlagani uchun connection errorlarni oldini olgani custum def pdate yasaldi)
![Screenshot from 2023-02-07 23-38-51](https://user-images.githubusercontent.com/109902921/217337343-eabe5b6e-05f7-47fe-a29e-874dbc06ce76.png)

## Result
![Screenshot from 2023-02-07 23-42-55](https://user-images.githubusercontent.com/109902921/217337318-1a07f5f4-4e1e-451f-832d-172cd225ae2b.png)


quyidagi func orqali USD ga nisbatan har qanday valyutada boshqa valyutaga pullarni ayri boshlash mumkin|
```
def convert(from_currency, to_currency, amount):
    with open('currency.json') as f:
        data = json.load(f).get('data')
    initial_amount = amount

    if from_currency != 'USD':
        amount = amount / data.get(from_currency)

    amount = round(amount * data[to_currency], 2)
    res = ('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
    return res
```
