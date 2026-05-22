



password = 123456
count = 3


while True:
    count -= 1
    password_input = int(input('Nhập mật khẩu:'))

    if password_input == password:
        print('Đăng nhập thành công!')
        break
    else:
        print('Mật khẩu sai . Xin vui lòng nhập lại.')
        print(f'Bạn chỉ còn {count} lần nhập')
    

    if count == 0:
        print('Tài khoản đã bị khóa')
        break