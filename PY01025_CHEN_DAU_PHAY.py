# Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.
# Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.
# Input
# Chỉ có 1 số N
# Outpu
# Kết quả sau khi đã chèn dầu phẩy

s = input()
for i in range(len(s)-3,0,-3):
    s = s[:i] + ',' + s[i:]
print(s)