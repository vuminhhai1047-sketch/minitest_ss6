
total_price = 0

price = int(input('Hãy nhập đơn giá cho sản phẩm:'))
quantity = int(input('Nhập số lượng mua:'))

total_price = price * quantity


if total_price >= 1000000:
    total_price = total_price * 0.9
elif total_price < 1000000:
    total_price


print('=' * 22 ,'ĐƠN THANH TOÁN' , '=' * 22)
print(f'Tổng số tiền mà bạn đã mua:{total_price}')
