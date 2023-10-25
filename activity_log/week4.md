<script type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$'], ['\\(','\\)']],
      processEscapes: true},
      jax: ["input/TeX","input/MathML","input/AsciiMath","output/CommonHTML"],
      extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
      TeX: {
      extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"],
      equationNumbers: {
      autoNumber: "AMS"
      }
    }
  });
</script>

# Week 4

# Table of Contents

0. Table of Contents
1. Introduction
2. Motivational Report Feedback
3. Varying Sample Size and Tumble Probability

See radial distribution function (probability) - see for Leonard Jones Fluid

clusters shown in GIFs last week are not isotropic


Attempt a reconstruction of features of systems without breaking any symmetries.


tumble rate against predicted tumble rate

Possibilities to pursue now:

#### 0. Prepare a dataset for CNN
#### 1. grid 2D ABP and bin the density
#### 2. Explore PDEs

$$\rho_{1}= D_{1}\nabla \rho_{1} + f_{1} (\rho_{1},\rho_{2},\rho_{3}) $$
$$\rho_{2}= D_{2}\nabla \rho_{2} + f_{2} (\rho_{1},\rho_{2},\rho_{3}) $$
$$\rho_{3}= D_{3}\nabla \rho_{3} + f_{1} (\rho_{1},\rho_{2},\rho_{3}) $$

Current step: explore; vary along density (0.01 to 0.5; choose logarithmic) and tumble probablity (10 values)

# 1. Introduction

The aim of this week is to consolidate the work of previous weeks and to build up qualitative understanding from it. The two tasks are:

1. Look over supervisor feedback for the motivational report from last week
2. Make a 5x5 configuration grid of particle system from [Week 3](./week3.qmd), varying tumble probability and particle number.
3. Combine results with lab partner
4. Plot total orientation against time
5. Look into clustering analysis

# 2. Motivation Report Feedback

I have created a separate website for monitoring development of the Motivational Report [here](./../motivational-report/motivational-report.qmd), also accessible through the sidebar. I will address every piece of feedback below.

# 3. Varying Sample Size and Tumble Probability


