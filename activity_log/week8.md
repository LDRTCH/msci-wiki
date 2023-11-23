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

# Week 8

# 0. Table of Contents

0. Table of Contents
1. Introduction
2. Project Plan
3. Tumbling Rate Clarifications
4. Dissipation and Structure
5. Further Information
6. Interim Report

# 1. Introduction

The main aim of this week is to finish the Interim Report. As this is not summative for us, the deadline has proven to not be strict - nonetheless I aim to finish it in time.

The secondary aim is to clarify various things that have come up throughout the past weeks, first and foremost the general plan of this project. The project plan is outlined below; we are currently still in the Characterisation phase. Percolation and pair-correlations are high priority in order to understand energy dissipation and to then transition into CNN construction.

# 2. Project Plan

These are some notes taken during open discussion between us and our supervisor.

1. Characterisation - set the landscape of physical properties by analysing the given Persistent Exclusion Process model

- timescales

- $\rho$-$P_{tumble}$ diagram

- cluster distibution

- percolation

- **pair-corelations** -> link to dissipation

2. Construction - make a minimal Convoluted Neural Network (CNN) model; retrieve physical properties from data analysis

- input details

	- ignore orientations (experiment-like): only use particle positions
	
	- include everything: particle orientations and positions

- pull information from steady-state systems

- validate the architecture

	- how do we choose architecture options?
	
		- map size
		
		- layer number
	
	- how much data? can we minimise it?
	
	- how does it extrapolate?
	
- explainability

	- compare with feature maps
	
	- check with explicit ways of measuring dissipation

3. Extension

- use CNN on non-steady state systems

	- chart applicability on transition into steady state
	
- extend CNN use to off-lattice models

# 3. Tumbling Rate Clarifications

In [Week 7](./week7.qmd), I mentioned some potential issues with $P_{tumble}$. This was due to a misunderstanding of the role this variable plays. To reiterate, $P_{tumble}$ is the probability that a particle will tumble in any direction, **including** the one it is already going into. This means that $P_{tumble}$ is related, but not synonimous, to the **rate of changing orientation**, because the former has a 25% chance to effectively 'tumble in place'. This is not an oversight of the model, it is a characteristic of analogising to random thermal fluctuations. Departure from equilibrium is caused as $P_{tumble}$ departs from $P_{tumble}^{max}=1$, irrespective of the probability of actually *changing* direction.

This clarification is useful to keep in mind as we begin talking about energy dissipation.

# 4. Dissipation and Structure

There is a prominent link between the structure of an active matter system and energy dissipation. Here energy dissipation is understood as the breaking of detailed balance; we can follow the argument below to trace expression of energy dissipation in terms of structural characteristic $P_{tumble}$:

$$P_{tumble}\sim \frac{1}{\tau} \sim \frac{1}{P_e} \sim \frac{1}{v_{active}}$$
where $\tau$ is the persistence time, $P_e$ is the Peclet number and $v_{active}$ is active velocity; the latter can be rephrased as a force using a friction coefficient, thereby giving us a 'negative friction'. Thus the link between dissipation and the tumbling rate is established: a decrease in tumbling rate is an increase in detailed balance breaking, which is an increase in dissipation.

There are specific relations we can use to infer dissipation; these will be analysed in subsequent weeks.

# 6. Bin Count Grid

Using the cluster analysis shown in [Weeks 5-6](./week5-6.qmd), we can obtain cluster distribution relations as we vary the tumbling rate and the density. For the following grid of particle distributions:

<object data="./week-8-files/gridcorrect2.pdf" type="application/pdf" width="1000px" height="1000px">
     <embed src="./week-7-files/gridcorrect2.pdf">
         <p>Could not load PDF.</a>.</p>
     </embed>
 </object>

we get the following cluster grid:

<object data="./week-8-files/histogrid.pdf" type="application/pdf" width="1000px" height="1000px">
     <embed src="./week-7-files/histogrid.pdf">
         <p>Could not load PDF.</a>.</p>
     </embed>
 </object>



# 7. Interim Report

This is an almost finished version of the interim report, after applying some preliminary supervisor feedback. The finalised version will be done next week. There are some points that should be elaborated regarding CNN functionality, MIPS, percolation, pair correlation function as well as slightly revising the Discussion.
<object data="./week-8-files/Interim_Report-5.pdf" type="application/pdf" width="1000px" height="1000px">
     <embed src="./week-7-files/Interim_Report-5.pdf">
         <p>Could not load PDF.</a>.</p>
     </embed>
 </object>
