y_std = 30
m_std = 60
y_total = 0
m_total = 0

n = int(input())
times = list(map(int, input().split()))

for time in times:
    y_v = time // y_std
    m_v = time // m_std
    y_total += (y_v + 1)
    m_total += (m_v + 1)

y_fee = y_total * 10
m_fee = m_total * 15

if y_fee < m_fee:
    print('Y', y_fee)
elif y_fee > m_fee:
    print('M', m_fee)
else:
    print('Y M', y_fee)