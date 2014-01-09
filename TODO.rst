Functionality
========================

- make and base.save_system(<seed_name>)
  TODO: make sure .reloading is more sugar-coated,
  e.g. check for correct size of file and document
- make sure one can (re)start and stop viewer from ipython ('kmos run')
- kmos.gui.Editor should be able to process
  project_tree passed in automatically
  (and save changes directly to it)
  [should be transparent to the user]
- add a tags field to all entities: parameters, process, species, layer
- change book-keeping/memory management from
  process based to site based
  (better storage for amorphous geometries)
- add/fix undo function to process editor
- improve layer editor: make handling better (removing/cancelling sites)
  and make better guess for z-position of site
- improve speed by inlining function call in generated code
  [keep it optional in case inlining increases code base too much]
- put XML/DTD handling into stdlib only tools (validation currenty not supported)
- add convenience function to write time series
- document running of simulations better


Project related
========================

- configure pip mechanism
- build virtualenv test environment(s): 2.4-3.0
- build deb package

Future/optional projects
=========================

- do 3D version of process editor using ASE
  facilities first: basically rid gtkcanvas
  in favor or pygoocanvas and include atoms
  in background
- check-out blender and maybe additional 3D programs
  for good gui design of placing sites or species
  in 3D space


Defered
========================

- build-up library of lattices which can be
  simply chosen from (making new lattice is very easy
  and fast)

Refactorization
========================

- remove output functionality
