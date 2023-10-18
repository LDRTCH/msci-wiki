# Week 3

#0. Table of Contents

0. Table of Contents
1. Goals
2. Configuring BlueCrystal4

#1. Goals

The main aim of this week is to begin reproducing a simple active matter system in code. To this end, a suitable environment to work in must be found and utilised. For now we are primarily sticking to python.

We have gained access to the Bristol supercomputers BlueCrystal4 and BluePebble (I have access to the former, my lab partner has access to the latter). We will attempt to apply the scripts to the supercomputers.

In [Week 2](https://ldrtch.github.io/msci-wiki/activity_log/week2.html) it was suggested that I would go more in depth in statistical analysis. This has been put aside for now, in the interest of getting a feel for how ABP simulations work in practice. 

#2. Configuring BlueCrystal4 

I already have access to BlueCrystal4 (BC4) due to one of my other modules. For that particular module, I am programming in C/C++; as such, I have already configured (installed and loaded) modules compatible with it. These modules are generally installed on a user instance, and loaded using the following bash command:
`module load <path>`. For example, for loading the necessary files for Intel's C/C++ compiler (icc), I use the following: `module load languages/intel/2020-u4`.

The issue that arises is that, at least initially, we have decided to work in Python. While I plan to attempt to translate (and speed up) our later codes in C, it is preferable to agree on a shared language while we get our bearings (and Python is easier, for all its faults). I therefore need use both C and python modules; hopefully this will not cause conflicts as long as they are not loaded simultaneously. The loading can easily be done in the `.bashrc` script on the user home instance, which will keep the module loaded for any and all processes. This is inadvised in the BC4 user manual, however - like I said, conflicts can occur. It is much healthier and safer to instead load modules in the `.sh` script that will send a request to the job queue. This will be elaborated on later.

You load/add modules with `module load` or `module add`. I have used the former for C and the latter for Python, though strictly to differentiate the two better. Below is a quick list of the different module commands I use:
```bash
module avail #Lists available modules; can combine with grep to search for a specific one

module load languages/intel/2020-u4 #Loads icc for C/C++
module add languages/anaconda3/2022.11-3.9.13-tensorflow-2.11 #Loads anaconda tensor flow package
module add languages/anaconda3/2020−3.8.5 #Loads full anaconda package
curl https://pyenv.run | bash #Loads python environment (non-anaconda alternative)

#NOTE: only one of these should be done for any instance!

module list #Lists loaded modules
```

Tested a quick "Hello, World!" program just to make sure that python runs correctly; it does, at least for now.

### 3. Small Github Digression
A few things need to be said about the exact

For connecting to organisation projects that I clone locally, the following commands are useful:
```bash

```


