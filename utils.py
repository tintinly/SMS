import re
import pyperclip
from win10toast import ToastNotifier

def extract_first_long_number(text):
    # 匹配长度大于等于4的数字字符串
    pattern = r'\d{4,}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None

def match_Captcha_number(text):
    # 匹配app和验证码
    pattern = r'(【\S*】).*(\d{4,})'
    match = re.search(pattern, text)
    if match:
        return match
    return None


def show_toast_notification(title, message, duration=3):
    # 创建通知对象
    toaster = ToastNotifier()
    # 显示通知，duration表示通知持续的时间（秒）
    toaster.show_toast(title, message, duration=duration, threaded=True)


def copy_verification_code(text):
    match = match_Captcha_number(text)
    app = match.group(1)
    number = match.group(2)
    if number:
        # 复制到剪贴板
        pyperclip.copy(number)
        print(f"已复制到剪贴板: {number}")
        # 显示通知
        show_toast_notification("复制成功", text)
        return number
    else:
        print("未找到符合条件的数字字符串")
        # 显示通知
        show_toast_notification("复制失败", f"请检查短信验证码")
        return None
    


if __name__ == "__main__":
    text = "这是一段包含数字1234、56789和100的文本。"
    copy_verification_code(text)