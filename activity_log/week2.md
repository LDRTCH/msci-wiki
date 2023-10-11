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


# Week 2

### Table of Contents

###### 0. Table of Contents
###### 1. Introduction
###### 2. Deadline Schedule
###### 3. Text Information 
###### 4. Motivation Report

###1. Introduction

The goal of week 2 is to further familiarise ourselves with the literature. We are to write a quick 500-word referenced report detailing motivations for studying active matter. Notes for this week will therefore be slightly sparser, primarily sifting through the goals of various papers (their detailed processes are to be examined at a later date). Some of these tidbits of information will be taken from the texts explored in week 1; as such, overlap with week 1 information is not only possible, but very likely. Repetition was preferred over disorganised and uncatalogued information, as these notes serve both as an activity log (which must document repeats occasionally) and as a catalogue of information as it is found.

Another essential goal of weeks 1 and 2 was to figure out the general examination schedule of the project. This in turn would influence planning the project out more properly, in anticipation of the deadline for the interrim report (other influences, naturally, are personal academic schedules; I personally anticipate being much busier during the first term, and therefore expect higher activity during the latter half of the project). This schedule was not given out to the 30cp version of the project page until very recently, and has therefore been appended in the activity log for this week.

Above is a table of contents. Below is a list of a few of the utilised texts, with some key information extracted. The 500-word referenced essay is given afterwards. At the very bottom is a very brief introduction to the Langevin equation. On an informational level, this is meant as a way to ease in into Brownian motion theory; on a technical level, this also gives a brief occasion to experiment with LaTex in markdown. 

### 2. Deadline Schedule

- Week 1: Start of project
- Week 9: Optional interim report submitted. Formative only. Deadline is Thursday 23th November @ 12.30pm.
- Week 19: Practical work (experimental or computational/theoretical) must finish by the end of the week. Friday 8th March.
- Weeks 20/21: Analysis of results obtained. Start write up of report. Results to be presented to supervisor and analysis discussed.
- Week 22: Final Report submission. Deadline is Thursday 18th April @ 12.30pm.
- Weeks 23/24: Final interviews with Assessors and supervisors. **Assessment**: The final assessment is worth 100% of the total marks available.

(This schedule will be added on the website as a separate tab as well.)

### 3. Text information

#### The Mechanics and Statistics of Active Matter

This is a 2010 review of (at the time) recent progress within the field. Its main role for my current purposes is to obtain references to older papers (and therefore to their motivations), while also providing a starting definition for active matter.

- active matter can be considered as a type of material

- take active matter as condensed matter in a **nonequilibrium regime**

	- each (autonomous/active) constituent takes direct energetic input
	
		- energy input is therefore homogenously distributed in system
		
		- compare to fluid motion, for instance: energy is not supplied to each individual particle, but rather is applied (e.g. kinetically) at the boundaries: this then causes particles to push others forward, but they don't all have direct access to energy
		
		- slightly related, Ramaswamy argues in one of his [lectures](https://www.youtube.com/watch?v=o2YlVQsyIpc) that this is the key distinction of active matter, phrased as **direct access to energy** (in the fluid example above, the bulk particles have **indirect** access to energy)
	
	- force-free: forces exerted between particle and fluid cancel
	
	- (self-propelled) motion is set by particle, not external fields 

#### Catalytic Nanomotors: Autonomous Movement of Striped Nanorods, Paxton, Kistler et al.

This is a 2004 paper experimentally confirming a solution to the convection-diffusion relation applied to rod-shaped particles (with Pt and Au segments) moving autonomously in hydrogen peroxide solutions.

- one of the big nanotechnology challenges is the conversion of stored chemical technology to motion	
	
	- this is precisely what many biological active matter systems do
	
	- studying this would yield useful artifficial active matter systems

#### Active matter: quantifying the departure from equilibrium, Flenner & Szamel

This is a 2020 paper examining active matter systems as they are moved further away from thermodynamic equilibrium.

- the main motivational point here is that 


### 4. Motivation Report

Active matter is, broadly, a subcategory of matter systems distingushed primarily by energy input homogenously distributed across all constituents (agents) of the system, which in turn set their own self-propelled motion across a force-free medium (for instance, the forces between particles and the fluid they move through cancel)[1]. The agents therefore have *direct* access to energy, and use it to autonomously propel and direct themselves (with different models and situations allowing for various degrees of freedom). The study of active matter is generally grounded in (but not limited to) observed behaviour of biological agents, as they are the primary (though not only) examples of active matter in nature. 

The evident motivation in studying active matter is that it helps understand biological behaviours, and therefore the natural world. Macroscopically, the construction of theoretical models can help explain, and to a limited degree predict, the behaviour of animals (such as locusts) undergoing collectively-emergent swarming behaviours (where each animal can be treated as its own autonomous agent, sharing the same generally stable 'rules' of altering speed and orientation while interacting with each other and the environment)[2]. This is not limited to what can be termed 'simple' behaviour; human behaviour can be partially mapped and understood within physically-indexed accounts of autonomous choices within (overtly or suggestively) constrained collective action. Interesting examples are swarming behaviours identified in traffic, crowd disasters and concerts[3] (note however that physical models are sometimes challenged in literature due to potential oversimplifications, insofar as, for instance, cognitive heuristics under duress might deal holistically, rather than individually, with other human agents[4]).  Microscopically, active matter models offer insight into understanding how hierarchically-organised emergence happens within cell tissues, and how it may be leveraged by medicine[5].

Outside of biology, active matter research serves to emulate, or otherwise learn from, naturally-occurring behaviours in order to analyse a potentially more general thermodynamic state. Due to the necessarily dissipative use of energy within self-organised agents, and their internally-induced behaviour, active matter is not described by the statistical mechanics of equilibrium states. The question then arises whether, through quantitative computation and qualitative modelling/theorising, the thermodynamic laws of equilibria can be modified and generalised to non-equilibrium states, and how these generalisations hold as departure from equilibrium through various means is increased[6]. These generalisations would, ideally, collapse into the known statistical thermodynamics states within the equilibrium limit. These insights, in turn, would facilitate the creation of synthetic active matter, whose potential, although speculatory, ranges from the biomedical application of nanomachine targeted drug delivery possibilities to the location-mapping application of nanoscopic/microscopic enivronmental sensing[7]. 

The feature in active matter of converting stored and homogenously available energy, such as chemical potential, into mechanical work is also of great importance to the field: understanding how this can work and how to facilitate, among other things, long-term energy access across the active matter substance is a key pursuit of nanotechnology[8]. Statistical and computational models can lend insight into individual and collective dynamics, and in turn give way to new experimental designs of nano/micromechanical systems. 

<br>

502 words.
<br> 
#### References
1. Active matter: quantifying the departure from equilibrium. Flenner & Szamel

2. From Disorder to Order in Marching Locusts. Buhl et al. (2006)

3. Collective Motion of Humans in Mosh and Circle Pits at Heavy Metal Concerts. Silverberg et al. (2013)

4. How simple rules determine pedestrian behavior and crowd disasters. Moussaid, Helbing & Theraulaz (2011)

5. Active matter at the interface between materials science and cell biology. Needleman & Zvonimir (2017)

6. Phase Separation and Multibody Effects in Three-Dimensional Active Brownian Particles. Turci & Wilding (2021)

7. Nano/Micromotors in Active Matte. Lv, Yank & Li (2022)

8. Catalytic Nanomotors: Autonomous Movement of Striped Nanorods, Paxton et al. (2004)

### 5. Langevin Equation

The **Langevin equation** represents the partly-random particle movement of a particle within a fluid:
	
$$m \frac{dv}{dt}=-\lambda \mathbf{v} +\boldsymbol{\eta} (t)$$
where $\textbf{v}$ is particle velocity, $\lambda$ is the damping coefficient, m is the particle mass, $\boldsymbol{\eta}$ is the **noise term**.

The **noise term** indicates collisions of the given particle with other molecules within the fluid. It is determined by a Gaussian distribution, and for the Boltzmann constant $k_{B}$, temperature $T$ and $\eta_{i}$ being the i-th component of vector $\boldsymbol{\eta}(t)$, it is described by the following correlation function:

$$\langle \eta_{i} (t) \eta_{j} (t')\rangle = 2 \lambda k_{B} T \delta_{i,j} \delta(t-t')$$

This approximates that any given force (at time $t$) is uncorrelated with a force at any other time. The collision time with other molecules indicates this is not the case. However, within great collective motion this is broadly the case. The appearance of the damping coefficient $\lambda$ in the correlation function is, *within an equilibrium system*, an expression of the **Einstein relation**.
