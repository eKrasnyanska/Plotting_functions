import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import pandas as pd

dpii = 80
fig = plt.figure(dpi=dpii, figsize=(1024 / dpii, 568 / dpii))
mpl.rcParams.update({'font.size': 12})

plt.axis([-50, 50, 0, 10])

plt.title('Natural logarithm')
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

xs = []
fx = []

x = -50.0
while x <= 50.1:
    fx += [math.log(pow(x, 2)+3)]
    xs += [x]
    x += 0.1

df = pd.DataFrame({'x': xs, 'f(x)': fx})
df.to_csv('result.csv', sep=';', index=False, header=False)

plt.plot(xs, fx, color='blue', linestyle='solid',
         label='ln(x^2+3)')

plt.legend(loc='upper right')
fig.savefig('trigan.png')
