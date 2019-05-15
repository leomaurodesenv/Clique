"""
@module: Cluster
This module is cluster structure

@authors: György Katona <georgekatona>, Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/Clique GitHub
@license: MIT License 
@copyright: 2019 György Katona
@package: Clique
@access: public
"""

class Cluster:
    ''' Cluster Class '''

    def __init__(self, dense_units, dimensions, data_point_ids):
        ''' 
        Cluster object construtor
        @param dense_units: 
        @param dimensions: 
        @param data_point_ids: 
        '''
        self.id = None
        self.dense_units = dense_units
        self.dimensions = dimensions
        self.data_point_ids = data_point_ids

    def __str__(self):
        ''' 
        Cluster stringfy
        @return: Cluster information
        '''
        return "Dense units: " + str(self.dense_units.tolist()) + "\nDimensions: " \
               + str(self.dimensions) + "\nCluster size: " + str(len(self.data_point_ids)) \
               + "\nData points:\n" + str(self.data_point_ids) + "\n"
