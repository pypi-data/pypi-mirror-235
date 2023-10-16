from cbx.dynamics.pdyn import ParticleDynamic
import pytest
import numpy as np
from test_abstraction import test_abstract_dynamic
from cbx.utils.objective_handling import cbx_objective_fh

class Test_pdyn(test_abstract_dynamic):
    
    @pytest.fixture
    def dynamic(self):
        return ParticleDynamic
    
    def test_term_crit_maxit(self, dynamic, f):
        '''Test termination criterion on max iteration'''
        dyn = dynamic(f, d=5, max_it=7)
        dyn.optimize()
        assert dyn.it == 7

    def test_no_given_x(self, dynamic, f):
        '''Test if x is correctly initialized'''
        dyn = dynamic(f, d=5, M=4, N=3)
        assert dyn.x.shape == (4,3,5)
        assert dyn.M == 4
        assert dyn.N == 3

    def test_given_x_1D(self, dynamic, f):
        '''Test if given x (1D) is correctly reshaped'''
        dyn = dynamic(f, x=np.zeros((7)), max_it=1)
        assert dyn.x.shape == (1,1,7)
        assert dyn.M == 1
        assert dyn.N == 1

    def test_given_x_2D(self, dynamic, f):
        '''Test if given x (2D) is correctly reshaped'''
        dyn = dynamic(f, x=np.zeros((5,7)), max_it=1)
        assert dyn.x.shape == (1,5,7)
        assert dyn.M == 1
        assert dyn.N == 5

    def test_opt_hist_and_output(self, dynamic, f):
        '''Test if optimization history is correctly saved and output is correct'''
        dyn = dynamic(f, x = np.zeros((6,5,7)), max_it=10, save_int = 3, track_list=['x'])
        x = dyn.optimize()
        assert dyn.history['x'].shape == (5,6,5,7)
        assert x.shape == (6,7)
        assert dyn.x.shape == (6,5,7)

    def test_f_wrong_dims(self, dynamic):
        '''Test if f_dim raises error for wrong dimensions'''
        def f(x): return x
        f_dim = '1D'
        x = np.random.uniform(-1,1,(6,5,7))

        with pytest.raises(ValueError):
            dynamic(f, x=x, f_dim=f_dim)
            
    def test_torch_handling(self, f, dynamic):
        '''Test if torch is correctly handled'''
        import torch
        x = torch.zeros((6,5,7))
        
        @cbx_objective_fh
        def g(x):
            return torch.sum(x, dim=-1)
        
        dyn = dynamic(g, x=x, max_it=2, array_mode='torch')
        dyn.optimize()
        assert dyn.x.shape == (6,5,7)

    

