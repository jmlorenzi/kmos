model_name = 'test_cli_generated_model'
simulation_size = 20
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "p_CO":{"value":"0.2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"log"},
    "T":{"value":"500", "adjustable":True, "min":"0.0", "max":"0.0","scale":"linear"},
    "p_O2":{"value":"1.0", "adjustable":True, "min":"0.0", "max":"0.0","scale":"linear"},
    }

rate_constants = {
    "CO_adsorption":("1000.", True),
    "CO_desorption":("1000.", True),
    }

site_names = ['default_cus']
representations = {
    "CO":"""""",
    "empty":"""""",
    "oxygen":"""""",
    }

lattice_representation = """"""

species_tags = {
    "CO":"""""",
    "empty":"""""",
    "oxygen":"""""",
    }

tof_count = {
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 2)">
    <meta author="Max J. Hoffmann" debug="0" email="mjhoffmann@gmail.com" model_dimension="2" model_name="test_cli_generated_model"/>
    <species_list default_species="empty">
        <species color="#000000" name="CO" representation="" tags=""/>
        <species color="#ffffff" name="empty" representation="" tags=""/>
        <species color="#ff0000" name="oxygen" representation="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="True" max="0.0" min="0.0" name="T" scale="linear" value="500"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="p_CO" scale="log" value="0.2"/>
        <parameter adjustable="True" max="0.0" min="0.0" name="p_O2" scale="linear" value="1.0"/>
    </parameter_list>
    <lattice cell_size="1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0" default_layer="default" representation="" substrate_layer="default">
        <layer color="#ffffff" name="default">
            <site default_species="default_species" pos="0.0 0.5 0.5" tags="" type="cus"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="CO_adsorption" rate_constant="1000.">
            <condition coord_layer="default" coord_name="cus" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="cus" coord_offset="0 0 0" species="CO"/>
        </process>
        <process enabled="True" name="CO_desorption" rate_constant="1000.">
            <condition coord_layer="default" coord_name="cus" coord_offset="0 0 0" species="CO"/>
            <action coord_layer="default" coord_name="cus" coord_offset="0 0 0" species="empty"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
