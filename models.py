# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:29:55 2016

@author: danielg
"""
#necessray modules: numpy, matplotlib, math

import numpy
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import math



#names of variables:
#eg = exponential growth
#dg = discrete generations
#cg = continuous generations
#gr = growth rate
#x = population
#t = time




#General_Parameters

#initial population
i_pop = 3.0

#final_population\
f_pop = 1000.0

# g r> 1
pos_gr_1 = 1.2

# 0 < gr < 1

pos_gr_2 = 0.312

# gr < -1 

neg_gr_1 = -1.2

# -1 < gr < 0

neg_gr_2 = -0.312

# dictionary with the growth rates that are to be evaluated on each model (totally editable, put a description and value)

gr_dict = {'pos_gr_1':pos_gr_1, 'pos_gr_2':pos_gr_2, 'neg_gr_1':neg_gr_1, neg_gr_2:neg_gr_2}

#time if continuous or generations if discrete

t = 100.



class eg_dg:
    '''Exponential growth with continuous generations. pg.4. 
    x' = Rx
    
    negative values of gr don't conform to an exponential
    growth. They were only included here for curiosity, should be ignored if one is dealing with populations (postive and negative
    come from an odd or even exponent).
    in general, 0<gr<1 exhibit exponential decay, whereas gr>1, exhibits exponential growth.
    
    Becuase the population conform to discrete units, the function is not differentialble. Nevertheless, if one considers
    large population densities, the jumps caused by individual births and deaths are negligible, which allows us to postulate the
    existence of a time derivative'''
    def __init__(self, i_pop, t, description= 'Exponential growth with discrete generations'):
        self.i_pop = i_pop
        self.t = t
        self.description = description
        
    def describe(self, text):
        self.description = text
    
    def generation(self, t):
        self.t = t
    
    def i_pop(self, i_pop):
        self.i_pop = i_pop
        
    def model(self, gr, t):
        return ((gr)**t)*self.i_pop
    
    
    def general_behaviour_plot(self, gr_dict): 
        '''plots for three scenarios for the gr given as a dictionary of inputs'''
        time_axis = numpy.arange(1,self.t)
        f, axarr = plt.subplots((len(gr_dict)+1)/2,(len(gr_dict)+1)/2)
        plot_indexes = [(m,n) for m in xrange((len(gr_dict)+1)/2) for n in xrange((len(gr_dict)+1)/2) ]
        f.suptitle(self.description, fontsize=12)
        for x in xrange(len(gr_dict.keys())):
            population = [self.model(gr_dict[gr_dict.keys()[x]], time) for time in numpy.arange(1,self.t)]
            axarr[plot_indexes[x][0],plot_indexes[x][1]].plot(time_axis, population, label='growth_rate = %.2f' %gr_dict[gr_dict.keys()[x]]) 
            axarr[plot_indexes[x][0],plot_indexes[x][1]].legend(loc='upper center')
            axarr[plot_indexes[x][0],plot_indexes[x][1]].set_xlabel('generations')
            axarr[plot_indexes[x][0],plot_indexes[x][1]].set_ylabel('population')
        plt.show()
    def parameter_space(self):
        self.i_pop = 50
        growth_rate_range = numpy.linspace(-2,2, 25)
        f, axarr = plt.subplots(2,1)
        for i in xrange(len(growth_rate_range)):
            population = [self.model(growth_rate_range[i], time) for time in xrange(20)]
            axarr[0].plot(numpy.arange(20), population)
            axarr[0].set_ylim(-5000,5000)
        for i in xrange(len(growth_rate_range)):
            population = numpy.array([self.model(growth_rate_range[i], time) for time in xrange(20)])
            axarr[1].semilogy(growth_rate_range[i], max(population), 'o')
            #axarr[1].set_ylim(-5000,5000)
        plt.show()


class eg_cg:
    '''Exponential growth with continuos generations. pg.4. '''
    def __init__(self, i_pop, f_pop, t, description= 'Exponential growth with continuous generations'):
        self.i_pop = i_pop
        self.f_pop = f_pop
        self.t = t
        self.description = description
        
        
    def describe(self, text):
        self.description = text
    
    def generation(self, t):
        self.t = t
    
    def i_pop(self, i_pop):
        self.i_pop = i_pop
    
    def f_pop(self, f_pop):
        self.f_pop = f_pop
        
    def model_derivative(self, gr, x):
        return gr*x
    
    def model_solution(self, gr,t):
        return self.i_pop*((math.e)**(gr*t))
    
    
    def derivative_behaviour_plots(self, gr_dict): 
        '''plots for three scenarios for the gr given as a dictionary of inputs'''
        population_axis = numpy.arange(1,self.f_pop) 
        f, axarr = plt.subplots((len(gr_dict)+1)/2,(len(gr_dict)+1)/2)
        plot_indexes = [(m,n) for m in xrange((len(gr_dict)+1)/2) for n in xrange((len(gr_dict)+1)/2) ]
        f.suptitle(self.description+'\nchange in the derivetive as a linear function of population size', fontsize=12)
        for x in xrange(len(gr_dict.keys())):
            growth_rate = [self.model_derivative(gr_dict[gr_dict.keys()[x]], pop) for pop in numpy.arange(1,self.f_pop)]
            axarr[plot_indexes[x][0],plot_indexes[x][1]].plot(population_axis, growth_rate, label='(per capita) growth_rate = %.2f' %gr_dict[gr_dict.keys()[x]]) 
            axarr[plot_indexes[x][0],plot_indexes[x][1]].legend(loc='upper center')
            axarr[plot_indexes[x][0],plot_indexes[x][1]].set_xlabel('population')
            axarr[plot_indexes[x][0],plot_indexes[x][1]].set_ylabel('dx(t)/dt')
        plt.show()
    
