* Replication do-file for analysis dataset "Populism as a social identity frame" *

* Replicates analyses performed in "The Effects of Populism as a Social Identity frame on Persuasion and Mobilization: Evidence from a 15-country experiment" 
* by Bos, Schemer, Corbu, Hameleers, Andreadis, Schulz, Schmuck, Reinemann, Fawzi
* To be published in European Journal of Political Research


** DATA PREPARATION **	

codebook 

** Sample Description
su gender age educ polint ideo

** Randomization Check, pooled

oneway age conditions, tab 
oneway gender conditions, tab
oneway educ conditions, tab
oneway ideo conditions, tab
oneway polint conditions, tab

** Remove Low Quality Respondents | see Appendix A

keep if finalflag == 0 



** Prepare scales 

	* persuasion

alpha issue1 issue2 

gen iss12 = (issue1 + issue2) / 2

	* mobilization

factor collact1 collact2 collact3, mineigen(1) pcf

alpha collact1 collact2 collact3

gen collact = (collact3 + collact1 + collact2)/3

	* relative deprivation

factor reldep1 reldep2 reldep3, mineigen(1) pcf

alpha reldep1 reldep2 reldep3

gen reldep = (reldep1 + reldep2 + reldep3)/3

	* descriptives 

su collact iss12 reldep

** Manipulation checks

oneway  mancheck1 heartland, tab bonferroni
oneway  mancheck3 heartland, tab bonferroni
oneway  mancheck8 heartland, tab bonferroni

oneway  mancheck4 antielite, tab bonferroni
oneway  mancheck6 antiim, tab bonferroni



** ANALYSES FOR RESULTS SECTION **

* H1a & H1b

reg iss12 antielite antiim ib8.Country_Code, robust cluster(Country_Code)

* H1c

reg iss12 antielite##antiim ib8.Country_Code, robust cluster(Country_Code)

* H2a & H2b

reg collact antielite antiim ib8.Country_Code, robust cluster(Country_Code)

* H2c

reg collact antielite##antiim ib8.Country_Code, robust cluster(Country_Code)

* H3a & H3b

regress iss12 antielite antiim  reldep ib8.Country_Code, robust cluster(Country_Code)

regress iss12 antielite##c.reldep antiim##c.reldep ib8.Country_Code  , robust cluster(Country_Code)

* H3c

regress iss12 antielite##antiim##c.reldep ib8.Country_Code  , robust cluster(Country_Code)

* H4a & H4b

regress collact antielite antiim  reldep ib8.Country_Code, robust cluster(Country_Code)

regress collact antielite##c.reldep antiim##c.reldep ib8.Country_Code  , robust cluster(Country_Code)


* Figure 3 *

regress collact antielite##c.reldep antiim##c.reldep ib8.Country_Code, robust cluster(Country_Code)

margins, dydx(antielite) at(reldep=(1 (0.33) 7)) vsquish post


marginsplot,  ///
title(" ") ///
xlabel(1 2 3 4 5 6 7, valuelabel) yline(0, lcolor(black))  ///
ylabel(-.8 -.7 -.6 -.5 -.4 -.3 -.2 -.1 0 .1 .2 .3 .4) yline(0, lcolor(black)) ///
b1title(relative deprivation, size (4)) xtitle ("") ///
ytitle(Effect of anti-elite cue) ///
legend(col(2) size(small)  order(2 1) label(2 "Marginal effect on mobilization") label(1 "95% Confidence Interval") ) ///
scheme (s2mono) name(fig_3a, replace)

regress collact antielite##c.reldep antiim##c.reldep ib8.Country_Code, robust cluster(Country_Code)

margins, dydx(antiim) at(reldep=(1 (0.33) 7)) vsquish post


marginsplot,  ///
title(" ") ///
xlabel(1 2 3 4 5 6 7, valuelabel) yline(0, lcolor(black))  ///
ylabel(-.8 -.7 -.6 -.5 -.4 -.3 -.2 -.1 0 .1 .2 .3 .4) yline(0, lcolor(black)) ///
b1title(relative deprivation, size (4)) xtitle ("") ///
ytitle(Effect of anti-immigrant cue) ///
legend(col(2) size(small)  order(2 1) label(2 "Marginal effect on mobilization") label(1 "95% Confidence Interval") ) ///
scheme (s2mono) name(fig_3b, replace)



grc1leg   fig_3a fig_3b , legendfrom(fig_3a) scheme(s2mono)



* H4c

regress collact antielite##antiim##c.reldep ib8.Country_Code  , robust cluster(Country_Code)



** COUNTRY ANALYSES (Appendix C) **


** first generate interaction terms for country plots

gen rdae = antielite * reldep
gen rdai = antiim * reldep

label variable rdae "Anti-elite * Relative deprivation"
label variable rdai "Anti-immigration * Relative deprivation"



gen aeai = antielite * antiim

label variable aeai "Anti-elite * Anti-immigration"

gen rdaeai = antielite * antiim * reldep

label variable rdaeai "Anti-elite * Anti-immigration * Relative deprivation"


label variable antielite "Anti-elite"

label variable antiim "Anti-immigration"



** H1a-c


regress iss12  antielite antiim if Country_Code == 1, robust

est store Austria

regress iss12  antielite antiim if Country_Code == 2, robust

est store France 

regress iss12  antielite antiim if Country_Code == 3, robust

est store Germany

regress iss12  antielite antiim if Country_Code == 4, robust

est store Ireland

regress iss12  antielite antiim if Country_Code == 5, robust

est store Israel 

regress iss12  antielite antiim if Country_Code == 6, robust

est store Italy
 
regress iss12  antielite antiim if Country_Code == 7, robust

est store Netherlands

regress iss12  antielite antiim if Country_Code == 8, robust

est store Poland 

regress iss12  antielite antiim if Country_Code == 9, robust

est store Spain

regress iss12  antielite antiim if Country_Code == 11, robust

est store Sweden

regress iss12  antielite antiim if Country_Code == 12, robust

est store Switzerland 

regress iss12  antielite antiim if Country_Code == 13, robust

est store UK

regress iss12  antielite antiim if Country_Code == 14, robust

est store Norway

regress iss12  antielite antiim if Country_Code == 15, robust

est store Romania 

regress iss12  antielite antiim if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons) xline(1) eform xtitle(Cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuep, replace)
 


regress iss12  antielite antiim aeai if Country_Code == 1, robust

est store Austria

regress iss12  antielite antiim aeai if Country_Code == 2, robust

est store France 

regress iss12  antielite antiim aeai if Country_Code == 3, robust

est store Germany

regress iss12  antielite antiim aeai if Country_Code == 4, robust

est store Ireland

regress iss12  antielite antiim aeai if Country_Code == 5, robust

est store Israel 

regress iss12  antielite antiim aeai if Country_Code == 6, robust

est store Italy
 
regress iss12  antielite antiim aeai if Country_Code == 7, robust

est store Netherlands

regress iss12  antielite antiim aeai if Country_Code == 8, robust

est store Poland 

regress iss12  antielite antiim aeai if Country_Code == 9, robust

est store Spain

regress iss12  antielite antiim aeai if Country_Code == 11, robust

est store Sweden

regress iss12  antielite antiim aeai if Country_Code == 12, robust

est store Switzerland 

regress iss12  antielite antiim aeai if Country_Code == 13, robust

est store UK

regress iss12  antielite antiim aeai if Country_Code == 14, robust

est store Norway

regress iss12  antielite antiim aeai if Country_Code == 15, robust

est store Romania 

regress iss12  antielite antiim aeai if Country_Code == 16, robust

est store Greece
 
 
 


coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim ) xline(1) eform xtitle(Combined cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuecop, replace)
 


grc1leg cuep cuecop, legendfrom (cuep) position(3) scheme (s2mono)



** H2a-c


regress collact  antielite antiim if Country_Code == 1, robust

est store Austria

regress collact  antielite antiim if Country_Code == 2, robust

est store France 

regress collact  antielite antiim if Country_Code == 3, robust

est store Germany

regress collact  antielite antiim if Country_Code == 4, robust

est store Ireland

regress collact  antielite antiim if Country_Code == 5, robust

est store Israel 

regress collact  antielite antiim if Country_Code == 6, robust

est store Italy
 
regress collact  antielite antiim if Country_Code == 7, robust

est store Netherlands

regress collact  antielite antiim if Country_Code == 8, robust

est store Poland 

regress collact  antielite antiim if Country_Code == 9, robust

est store Spain

regress collact  antielite antiim if Country_Code == 11, robust

est store Sweden

regress collact  antielite antiim if Country_Code == 12, robust

est store Switzerland 

regress collact  antielite antiim if Country_Code == 13, robust

est store UK

regress collact  antielite antiim if Country_Code == 14, robust

est store Norway

regress collact  antielite antiim if Country_Code == 15, robust

est store Romania 

regress collact  antielite antiim if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons) xline(1) eform xtitle(Cue impact on mobilization) ylabel(, angle(vertical))  legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuem, replace)
 
 
 


regress collact  antielite antiim aeai if Country_Code == 1, robust

est store Austria

regress collact  antielite antiim aeai if Country_Code == 2, robust

est store France 

regress collact  antielite antiim aeai if Country_Code == 3, robust

est store Germany

regress collact  antielite antiim aeai if Country_Code == 4, robust

est store Ireland

regress collact  antielite antiim aeai if Country_Code == 5, robust

est store Israel 

regress collact  antielite antiim aeai if Country_Code == 6, robust

est store Italy
 
regress collact  antielite antiim aeai if Country_Code == 7, robust

est store Netherlands

regress collact  antielite antiim aeai if Country_Code == 8, robust

est store Poland 

regress collact  antielite antiim aeai if Country_Code == 9, robust

est store Spain

regress collact  antielite antiim aeai if Country_Code == 11, robust

est store Sweden

regress collact  antielite antiim aeai if Country_Code == 12, robust

est store Switzerland 

regress collact  antielite antiim aeai if Country_Code == 13, robust

est store UK

regress collact  antielite antiim aeai if Country_Code == 14, robust

est store Norway

regress collact  antielite antiim aeai if Country_Code == 15, robust

est store Romania 

regress collact  antielite antiim aeai if Country_Code == 16, robust

est store Greece
 
 
 


coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim ) xline(1) eform xtitle(Combined cue impact on mobilization) ylabel(, angle(vertical))  legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuecom, replace)
 

grc1leg cuem cuecom, legendfrom(cuem) position(3) scheme(s2mono)


** H3a-c


regress iss12  antielite antiim reldep rdae rdai if Country_Code == 1, robust

est store Austria

regress iss12  antielite antiim reldep rdae rdai if Country_Code == 2, robust

est store France 

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 3, robust

est store Germany

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 4, robust

est store Ireland

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 5, robust

est store Israel 

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 6, robust

est store Italy
 
regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 7, robust

est store Netherlands

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 8, robust

est store Poland 

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 9, robust

est store Spain

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 11, robust

est store Sweden

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 12, robust

est store Switzerland 

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 13, robust

est store UK

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 14, robust

est store Norway

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 15, robust

est store Romania 

regress iss12  antielite antiim  reldep rdae rdai if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim reldep) xline(1) eform xtitle(Moderated cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuerdp, replace)
 


 

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 1, robust

est store Austria

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 2, robust

est store France 

regress iss12  antielite antiim aeai  reldep rdae rdai rdaeai if Country_Code == 3, robust

est store Germany

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 4, robust

est store Ireland

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 5, robust

est store Israel 

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 6, robust

est store Italy
 
regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 7, robust

est store Netherlands

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 8, robust

est store Poland 

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 9, robust

est store Spain

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 11, robust

est store Sweden

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 12, robust

est store Switzerland 

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 13, robust

est store UK

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 14, robust

est store Norway

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 15, robust

est store Romania 

regress iss12  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim reldep rdae rdai aeai) xline(1) eform xtitle(Moderated combined cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuecordp, replace)
 





grc1leg cuerdp cuecordp, legendfrom(cuerdp) position(3) scheme(s2mono)



** H4a-c


regress collact  antielite antiim reldep rdae rdai if Country_Code == 1, robust

est store Austria

regress collact  antielite antiim reldep rdae rdai if Country_Code == 2, robust

est store France 

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 3, robust

est store Germany

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 4, robust

est store Ireland

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 5, robust

est store Israel 

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 6, robust

est store Italy
 
regress collact  antielite antiim  reldep rdae rdai if Country_Code == 7, robust

est store Netherlands

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 8, robust

est store Poland 

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 9, robust

est store Spain

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 11, robust

est store Sweden

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 12, robust

est store Switzerland 

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 13, robust

est store UK

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 14, robust

est store Norway

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 15, robust

est store Romania 

regress collact  antielite antiim  reldep rdae rdai if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim reldep) xline(1) eform xtitle(Moderated cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuerdm, replace)
 


 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 1, robust

est store Austria

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 2, robust

est store France 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 3, robust

est store Germany

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 4, robust

est store Ireland

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 5, robust

est store Israel 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 6, robust

est store Italy
 
regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 7, robust

est store Netherlands

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 8, robust

est store Poland 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 9, robust

est store Spain

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 11, robust

est store Sweden

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 12, robust

est store Switzerland 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 13, robust

est store UK

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 14, robust

est store Norway

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 15, robust

est store Romania 

regress collact  antielite antiim aeai reldep rdae rdai rdaeai if Country_Code == 16, robust

est store Greece
 
 
 



coefplot (Austria, label(Austria)) (France, label(France)) (Germany, label(Germany)) ///
 (Ireland, label(Ireland)) (Israel, label(Israel)) (Italy, label(Italy)) (Netherlands, label(Netherlands)) ///
 (Poland, label(Poland)) (Spain, label(Spain)) (Sweden, label(Sweden)) (Switzerland, label(Switzerland)) ///
 (UK, label(United Kingdom)) (Norway, label(Norway)) (Romania, label(Romania)) ///
 (Greece, label(Greece)) , drop(_cons antielite antiim reldep rdae rdai aeai) xline(1) eform xtitle(Moderated combined cue impact on persuasion) ylabel(, angle(vertical)) legend(pos(3) col(1)) scheme (s2mono) ///
 name (cuecordm, replace)
 





grc1leg cuerdm cuecordm, legendfrom(cuerdm) position(3) scheme(s2mono)








