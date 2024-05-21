import socket
from datetime import datetime

MAX_BYTES = 65535
port = 9000

# إنشاء مأخذ UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ربط المأخذ بعنوان محدد (عنوان المهاجم)
sock.bind(('0.0.0.0', 9001))  # عنوان المهاجم كمثال

# استلام الرسالة من العميل
data, address = sock.recvfrom(MAX_BYTES)
text = data.decode('ascii')
print('Received message from client:', text)

# تعديل الرسالة (محاكاة هجوم)
modified_text = "Modified time: {}".format(datetime.now())
modified_data = modified_text.encode('ascii')

# إرسال الرد المعدل إلى العميل
sock.sendto(modified_data, address)
