# task 5
# 1st cell
vec1 = list(range(int(1e5)))
vec2 = list(range(int(1e5)))

# 2nd cell
# %%timeit
vec_x = []
for i in vec1:
    vec_x.append(vec1[i]*vec2[i])
result = sum(vec_x)

# task 6
# use task's 5th code
print(f"{result:.2e}")

# task 7
import numpy as np
vec3 = np.array(range(int(1e5)))
vec4 = np.array(range(int(1e5)))

result = np.dot(vec3, vec4)
print(f"{result:.2e}")

