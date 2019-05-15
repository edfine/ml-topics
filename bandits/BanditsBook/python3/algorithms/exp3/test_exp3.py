exec(compile(open("core.py").read(), "core.py", 'exec'))

import random

random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)
arms = [BernoulliArm(mu) for mu in means]
print(("Best arm is " + str(ind_max(means))))

f = open("algorithms/exp3/exp3_results.tsv", "w")

for exp3_gamma in [0.1, 0.2, 0.3, 0.4, 0.5]:
  algo = Exp3(exp3_gamma, [])
  algo.initialize(n_arms)
  results = test_algorithm(algo, arms, 5000, 250)
  for i in range(len(results[0])):
      f.write(str(exp3_gamma) + "\t")
      f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")

f.close()