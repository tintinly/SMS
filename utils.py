import re
import pyperclip
from win10toast import ToastNotifier



def extract_captcha1(text):
    # 4位到6位的验证码 开头
    pattern = r'(【\S*】)(\d{4,6})'
    match = re.search(pattern, text)
    if match:
        return match.group(2)
    return extract_captcha2(text)

def extract_captcha2(text):
    # 4位到6位的验证码 在“码”或“碼”字样后
    pattern = r'(【\S*】).*[码碼]+\D*(\d{4,6})'
    match = re.search(pattern, text)
    if match:
        return match.group(2)
    return extract_captcha3(text)

def extract_captcha3(text):
    # 4位到6位的验证码 任意
    pattern = r'\d{4,6}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None

def show_toast_notification(title, message, duration=3):
    # 创建通知对象
    toaster = ToastNotifier()
    # 显示通知，duration表示通知持续的时间（秒）
    toaster.show_toast(title, message, duration=duration, threaded=True)


def copy_verification_code(text):
    number = extract_captcha1(text)
    if number:
        # 复制到剪贴板
        pyperclip.copy(number)
        print(f"已复制到剪贴板: {number}")
        # 显示通知
        show_toast_notification(f"验证码复制成功: {number}", text)
        return number
    else:
        print("未找到符合条件的数字字符串")
        # 显示通知
        show_toast_notification("验证码复制失败，请检查", text)
        return None
    


if __name__ == "__main__":
    text = "【app】这是一段包含数字1234、56789和100的文本。"
    copy_verification_code(text)