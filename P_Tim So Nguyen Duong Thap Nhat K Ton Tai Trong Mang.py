def first_missing_positive(nums_str):
    nums = list(map(int, nums_str.split())) # Chuyển chuỗi thành danh sách các số nguyên
    n = len(nums)
    
    # Bước 1: Loại bỏ các số âm và các số lớn hơn n
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
            
    # Bước 2: Đánh dấu vị trí của các số dương đã xuất hiện
    for i in range(n):
        idx = abs(nums[i])
        if idx <= n:
            nums[idx - 1] = -abs(nums[idx - 1])
            
    # Bước 3: Tìm số dương đầu tiên chưa xuất hiện
    for i in range(n):
        if nums[i] > 0:
            return i + 1
        
    return n + 1

# Nhập chuỗi từ người dùng và gọi hàm để tính toán kết quả
nums_str = input("Nhap chuoi cac so nguyen: ")
result = first_missing_positive(nums_str)

# Xuất ra kết quả
print("So nguyen duong dau tien chua xuat hien la: ", result)