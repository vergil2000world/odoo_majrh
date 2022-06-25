{
    'name': 'ressources humaines usms',
    'version': '1.0',
    'category':'RH',
    'sequence': '-1',
    'summary': "Gestion des ressources humaines à USMS",
    'description': "",
    
    'depends': 
    [
        'base', 'hr'   
    ],
    'data':[
        'security/security.xml',
        'wizards/createv_view.xml',
        'views/maj_rh_employee_view.xml',
        'views/echellon_view.xml',
        'views/majrh_categorie_view.xml',
        'views/majrh_cadre_view.xml',
        'views/majrh_corps_view.xml',
        'views/majrh_echelon_view.xml','views/ville_view.xml','views/region_view.xml','views/qualifications_view.xml','views/etablissement_view.xml',
        'views/majrh_grade_view.xml','views/rhu_fonction_view.xml','views/res_diplome_view.xml',
        'views/majrh_grade_view.xml','views/association_view.xml','views/dash_view.xml',
        'views/rhu_avancement_view.xml'
    ],
     'installable': True,
    'application': True,
    'auto_install': False,
     'license': 'LGPL-3',
     'author': "TDI ENSA BM"
     
    
}