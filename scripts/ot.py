import rdflib as r, pygraphviz as gv, sys
import  importlib
from IPython.lib.deepreload import reload as dreload
import percolation as pe
#importlib.reload(g.loadMessages)
#importlib.reload(g.listDataStructures)
#importlib.reload(g.interactionNetwork)
#importlib.reload(pe.linkedData)
##dreload(pe,exclude="pytz")
#dreload(pe)

def G(S,P,O):
    g.add((S,P,O))
L=r.Literal
ot = r.Namespace("http://purl.org/socialparticipation/ot/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL
xsd = r.namespace.XSD

#ga=pe.makeBasicGraph()
#ga[0].namespace_manager.bind("ot", "http://purl.org/socialparticipation/ot/")    
#ga=pe.makeBasicGraph()
#ga[0].namespace_manager.bind("ot", "http://purl.org/socialparticipation/ot/")    

gas=pe.startGraphs(
        ["geral","legenda","redhum","fisan","tese","parsoc","dadlig","rc"],
        ["Ontologia do Trabalho (OT)","Legenda da OT", "Rede Humana",
                      "Física Antropológica","Tese de Doutoramento",
        "Participação Social", "Dados Ligados", "Redes Complexas" ],
        ("ot", "http://purl.org/socialparticipation/ot/")
            )
ga=gas["geral"]

pe.C([gas[i] for i in ("geral",)],ot.Physics,
     "Física",
     comment=["the natural science that involves the study of matter, its motion through space and time, and related concepts such as energy and force. More broadly, it is the general analysis of nature, conducted in order to understand how the universe behaves.","""Mathematics is the language used for compact description of the order in nature, especially the laws of physics. This was noted and advocated by Pythagoras, Plato, Galileo, and Newton.
     Physics theories use mathematics to obtain order and provide precise formulas, precise or estimated solutions, quantitative results and predictions. Experiment results in physics are numerical measurements. Technologies based on mathematics, like computation have made computational physics an active area of research.
     Ontology is a prerequisite for physics, but not for mathematics. It means physics is ultimately concerned with descriptions of the real world, while mathematics is concerned with abstract patterns, even beyond the real world. Thus physics statements are synthetic, while mathematical statements are analytic. Mathematics contains hypotheses, while physics contains theories. Mathematics statements have to be only logically true, while predictions of physics statements must match observed and experimental data."""],
     label_en="Physics")



pe.C([gas[i] for i in ("geral",)],ot.StatisticalPhysics,u"Física Estatística",
        superclass=ot.Physics,
        comment="Branch of physics that uses methods of probability theory and statistics",label_en="Statistical Physics")

pe.C([ga],ot.ComplexNetworksTheory,u"Teoria das Redes Complexas",superclass=ot.StatisticalPhysics,color="#F29999",
        comment="Complex networks area of scientific research",label_en="Complex Networks Theory")

pe.C([ga],ot.GraphTheory,u"Teoria dos Grafos",
        comment="the study of graphs, which are mathematical structures used to model pairwise relations between objects. (wikipedia, Jun/2015)",label_en="Graph Theory")

pe.C([ga],ot.ProbabilityTheory,u"Teoria das Probabilidades",
        comment="Probability theory is the branch of mathematics concerned with probability, the analysis of random phenomena.[1] The central objects of probability theory are random variables, stochastic processes, and events: mathematical abstractions of non-deterministic events or measured quantities that may either be single occurrences or evolve over time in an apparently random fashion. (wikipedia, Jun/2015)",label_en="Probability Theory")

pe.C([ga],ot.Topology,u"Topologia",
        comment="The study of topological spaces. It is an area of mathematics concerned with the properties of space that are preserved under continuous deformations, such as stretching and bending, but not tearing or gluing. Important topological properties include connectedness and compactness. A topological space may be defined as a set of points, along with a set of neighbourhoods for each point, that satisfy a set of axioms relating points and neighbourhoods. The definition of a topological space relies only upon set theory and is the most general notion of a mathematical space that allows for the definition of concepts such as continuity, connectedness, and convergence.[1] Other spaces, such as manifolds and metric spaces, are specializations of topological spaces with extra structures or constraints. Being so general, topological spaces are a central unifying notion and appear in virtually every branch of modern mathematics.",label_en="Topology")

pe.P([ga],ot.grounds,"fundamenta","grounds")
pe.L([ga],"Topologia","fundamenta","Teoria dos Grafos")
pe.L([ga],"Teoria das Probabilidades","fundamenta","Teoria dos Grafos")
pe.L([ga],"Teoria dos Grafos","fundamenta","Teoria das Redes Complexas")


pe.P([ga],ot.enables,"possibilita","enables")
pe.L([ga],"Megadados","possibilita","Teoria das Redes Complexas")


pe.C([ga],ot.Statistics,"Estatística",
        comment="""The mathematical study of the likelihood and probability of events occurring based on known information and inferred by taking a limited number of samples. (Wolfram)
        Statistics is the science of learning from data, and of measuring, controlling, and communicating uncertainty; and it thereby provides the navigation essential for controlling the course of scientific and societal advances (Davidian, M. and Louis, T. A., 10.1126/science.1218685, adopted by ASA - American Statistical Association.""",label_en="Estatistics")
pe.L([ga],"Estatística","possibilita","Teoria das Redes Complexas")

pe.C([ga],ot.ComputerScience,"Ciência da Computação",
        comment="the scientific and practical approach to computation and its applications.",label_en="Computer Science")
pe.L([ga],"Ciência da Computação","possibilita","Teoria das Redes Complexas")


pe.C([ga],ot.DataMining,u"Mineração de Dados",
        comment="the computational process of discovering patterns in large data sets involving methods at the intersection of artificial intelligence, machine learning, statistics, and database systems",label_en="Data Mining")
pe.C([ga],ot.BigData,u"Megadados",superclass=ot.ComputerScience,
        comment="Big data is a broad term for data sets so large or complex that traditional data processing applications are inadequate. Challenges include analysis, capture, data curation, search, sharing, storage, transfer, visualization, and information privacy. The term often refers simply to the use of predictive analytics or other certain advanced methods to extract value from data, and seldom to a particular size of data set. Accuracy in big data may lead to more confident decision making. And better decisions can mean greater operational efficiency, cost reductions and reduced risk.",label_en="Big Data")
pe.L([ga],"Mineração de Dados","fundamenta","Megadados")

pe.C([ga],ot.Transdisciplinarity,"Transdisciplinaridade",
        comment="Transdisciplinarity connotes a research strategy that crosses many disciplinary boundaries to create a holistic approach.",label_en="Transdisciplinarity")
pe.L([ga],"Transdisciplinaridade","possibilita","Teoria das Redes Complexas")

#######
# Rede complexa até Rede Social

pe.C([ga],ot.ComplexNetwork,"Rede Complexa",
        comment="The study of complex networks is a young and active area of scientific research inspired largely by the empirical study of real-world networks such as computer networks and social networks. (Wikipedia) \na frequently big network in the environment or for the consideration of the environment that they reside. (R. Fabbri)",label_en="Complex Network")
pe.P([ga],ot.dealsWith,"trata de","deals with")
pe.L([ga],"Teoria das Redes Complexas","trata de","Rede Complexa")

pe.C([ga],ot.RelationshipNetwork,
     u"Rede de Relacionamento",
     superclass=ot.ComplexNetwork,
     comment="Rede com grafo proveniente de vértices e relacionamentos entre pares deles. (R. Fabbri)",label_en="Relationship Network")

pe.C([ga],ot.InteractionNetwork,
     u"Rede de Interação",
     superclass=ot.RelationshipNetwork,
     comment="Rede com grafo proveniente de vértices e interações entre pares deles. (R. Fabbri)",label_en="Interaction Network")

pe.C([ga],ot.SocialNetwork,
     u"Rede Social",
     superclass=ot.RelationshipNetwork,
     comment="a social structure made up of a set of social actors (such as individuals or organizations) and a set of the dyadic ties between these actors.",label_en="Social Network")

pe.C([ga],ot.HumanSocialNetwork,
     u"Rede Social Humana",
     superclass=ot.SocialNetwork,color="#F29999",
     comment="a social network whoose social actors are human beings.",label_en="Human Social Network")

pe.C([ga],ot.Anthropology,
     u"Antropologia",
     comment="the study of humans. Its main subdivisions are cultural anthropology, which describes the workings of societies around the world, and biological anthropology, which concerns long-term development of the human organism.",
     label_en="Anthropology")


pe.C([ga],ot.BiologicalAnthropology,
     "Antropologia Biológica",
     superclass=ot.Anthropology,
     comment="also known as physical anthropology, is a scientific discipline concerned with the biological and behavioral aspects of human beings, their related non-human primates and their extinct hominin ancestors. It is a subfield of anthropology that provides a biological perspective to the systematic study of human beings.",
     label_en="Biological Anthropology")

pe.C([ga],ot.HumanBehavioralEcology,
     "Ecologia Behaviorista Humana",
     superclass=ot.BiologicalAnthropology,
     comment="also known as human evolutionary ecology, HBE applies the principles of evolutionary theory and optimization to the study of human behavioral and cultural diversity.",
     label_en="Human Behavioral Ecology")

pe.C([ga],ot.SocioculturalAnthropology,
     "Antropologia Sociocultural",
     superclass=ot.Anthropology,
     comment="used to refer to social anthropology and cultural anthropology together. Cultural anthropology has greater prominance in the USA, and  are holistic, oriented to the ways in which culture affects individual experience and provides a rounded view of the knowledge, customs, and institutions of a people. Social anthropology attempts to isolate a particular system of social relations and provide analytical bases to social life.",
     label_en="Sociocultural Anthropology")


pe.C([ga],ot.Human,
     "Humano",
     comment="the only extant members of the hominini clade of the great apes (the human clade, Homo genus); characterized by erect posture and bipedal locomotion, manual dexterity and increased tool use, and a general trend toward larger, more complex brains and societies.",
     label_en="Human")
pe.L([ga],"Antropologia","trata de","Humano")
pe.P([ga],ot.composes,"compõe","composes")
pe.L([ga],"Humano","compõe","Rede Social Humana")

pe.C([ga],ot.AnthropologicalPhysics,
     "Física Antropológica",color="#F29999",
     comment="the complex networks study to benefit the participant.",
     superclass=ot.ComplexNetworksTheory,
     label_en="Anthropological Physics")

pe.P([ga],ot.related,"relacionado","related")
pe.L([ga],"Física Antropológica","relacionado","Ecologia Behaviorista Humana")
pe.L([ga],"Física Antropológica","relacionado","Antropologia Sociocultural")
pe.L([ga],"Física Antropológica","trata de","Rede Social Humana")

pe.C([ga],ot.Sociology,
     "Sociologia",
     comment="the study of human social relationships and institutions. (UNC)",
     label_en="Anthropological Physics")
pe.L([ga],"Sociologia","trata de","Rede Social Humana")

pe.C([ga],ot.SocialParticipation,
     "Participação Social",color="#F229F9",
     comment="also social engagement or social involvement, social participation refers to one's degree of participation in a community or society.",
     label_en="Social Participation")
pe.L([ga],"Participação Social","trata de","Rede Social Humana")
pe.L([ga],"Física Antropológica","relacionado","Participação Social")

pe.C([ga],ot.SocialPsychology,
     "Psicologia Social",
     comment="the scientific study of how people's thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others.",
     label_en="Social Psychology")
pe.L([ga],"Psicologia Social","trata de","Rede Social Humana")
pe.L([ga],"Física Antropológica","relacionado","Psicologia Social")

pe.C([ga],ot.Psic,
     "Psicologia\nPsicanálise\nPsiquiatria"
     )
pe.L([ga],"Psicologia\nPsicanálise\nPsiquiatria","trata de","Rede Social Humana")


pe.C([ga],ot.LinkedData,
     "Dados Ligados",color="#F229F9",
     comment="also known as semantic web, studies methods for publishing structured data so that it can be interlinked and become more useful through semantic queries.",
     superclass=ot.ComputerScience,
     label_en="Linked Data")
pe.L([ga],"Dados Ligados","possibilita","Rede Social Humana")
pe.L([ga],"Dados Ligados","relacionado","Megadados")
pe.L([ga],"Dados Ligados","possibilita","Física Antropológica")


pe.C([ga],ot.ComputationalLinguistics,
     "Linguística Computacional",
     comment="an interdisciplinary field concerned with the statistical or rule-based modeling of natural language from a computational perspective.",
     superclass=ot.ComputerScience,
     label_en="Computational Linguistics")
pe.L([ga],"Linguística Computacional","possibilita","Rede Social Humana")


#############
# Propriedade "relacionado" é simetrica
# Propriedade fundamenta é subpropriedade de possibilita
pe.G(ga[0],ot.related,rdf.type,owl.SymmetricProperty)
pe.G(ga[0],ot.grounds,owl.subPropertyOf,ot.enables)


#####

pe.C([ga],ot.DoctorateThesis,
        "Tese de Doutorado",color="#F29999",
        comment_pt="tese com contribuição original e relevante.",
        label_en="Doctorate Thesis")
pe.P([ga],ot.area,"área","area")
pe.L([ga],"Tese de Doutorado","área","Teoria das Redes Complexas")

pe.C([ga],ot.AppliedPhysics,
        "Física Aplicada",
        superclass=ot.Physics,
        comment="physics which is intended for a particular technological or practical use.",
        label_en="Applied Physics")
pe.L([ga],"Tese de Doutorado","área","Física Aplicada")
pe.C([ga],ot.ComputationalPhysics,
        "Física Computacional",
        superclass=ot.Physics,
        comment="the study and implementation of numerical analysis to solve problems in physics for which a quantitative theory already exists.",
        label_en="Computational Physics")
pe.L([ga],"Tese de Doutorado","área","Física Computacional")


pe.C([ga],ot.Contribution,
        u"Contribuição",
        comment_pt="contribuição científica, tecnológica ou de difusão de conhecimento",
        label_en="Contribution")
pe.P([ga],ot.contributes,"contribui","contributes")
pe.L([ga],"Tese de Doutorado","contribui","Contribuição")


pe.C([ga],ot.Resource,
        u"Recurso",
        comment="informational resource",
        label_en="Resource")
pe.P([ga],ot.references,"referencia","references")
pe.L([ga],"Contribuição","referencia","Recurso")

pe.C([ga],ot.Contribution,
        "Tese de Doutorado",
        comment_pt="tese com contribuição original e relevante.",
        label_en="Doctorate Thesis")

pe.C([ga],ot.Article,"Artigo\nLivro\nTexto informal\nSoftware\nAlgoritmo\nArtefato Audiovisual",
        superclass=ot.Resource)


#############
# Data properties
pe.D([ga],ot.coreRationale,u"justificativa principal",xsd.string)
pe.D([ga],ot.rationale,u"justificativa",xsd.string)
pe.LD([ga],u"Tese de Doutorado",u"justificativa principal",u"xsd:string")
pe.LD([ga],u"Tese de Doutorado",u"justificativa",u"xsd:string")

pe.D([ga],ot.generalGoal,u"objetivo geral",xsd.string)
pe.D([ga],ot.goal,u"objetivo",xsd.string)
pe.LD([ga],u"Tese de Doutorado",u"objetivo geral",u"xsd:string")
pe.LD([ga],u"Tese de Doutorado",u"objetivo",u"xsd:string")


lspec=u"científica\ntecnológica\noriginal\nensino\nextensão"
pe.D([ga],ot.spec,lspec,xsd.bool)
pe.LD([ga],u"Contribuição",lspec,u"xsd:bool")


pe.D([ga],ot.description,u"descrição",xsd.string)
pe.LD([ga],u"Contribuição",u"descrição",u"xsd:string")
pe.LD([ga],u"Recurso",u"descrição",u"xsd:string")


pe.D([ga],ot.url,u"url",xsd.string)
pe.LD([ga],u"Recurso",u"url",u"xsd:string")


######
# LEGEND

pe.C([gas["legenda"]],ot.FOO,
        "Área Instrumental",color="#F229F9"
        )

pe.C([gas["legenda"]],ot.FOO,
        "Conceito Base",color="#F29999"
        )

pe.C([gas["legenda"]],ot.FOO,
        "Classe"
        )

pe.C([gas["legenda"]],ot.FOO1,
        "Superclasse"
        )
pe.C([gas["legenda"]],ot.FOO,
        "Subclasse"
        ,superclass=ot.FOO1
        )
pe.C([gas["legenda"]],ot.FOO,
        "dado"
        ,color="#A2F3D1"
        )
#pe.L([ga],"Classe","propriedade","Classe ou dado")
pe.P([gas["legenda"]],ot.propfoo,"propriedade","property")
pe.L([gas["legenda"]],"Classe","propriedade","Classe")
pe.L([gas["legenda"]],"Classe","propriedade","dado")

#B=ga[1].subgraph(nbunch=["Área Instrumental","dado",
#               "Conceito Base",
#               "Classe",
#               "Superclasse",
#               "Subclasse"],
#               name="cluster2",
#               style="filled",
#               color="#EEEEEE",
#               label="LEGENDA",
#               labelfontsize=40.)

#ga[1].add_node(1)
#ga[1].add_node(2)
#ga[1].add_node(3)
#ga[1].add_node(4)
#G1 = ga[1].subgraph(nbunch=[1,2],
#        name="cluster1",
#        style='filled',
#        color='lightgrey',
#        label='cluster 1 label')
#B.graph_attr['rank']='same'
#B.graph_attr['style']='filled'
#B.graph_attr['fillcolor']='#FF0044'
#B.graph_attr['color']='#FF0044'
#B.graph_attr['bgcolor']='#FF0044'

#######
# Escrita dos arquivos RDF e figuras PNG.

nome_="OT"
A=ga[1]
g=ga[0]
nome=("../figs/%s.png"%(nome_,))
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/%s_2.png"%(nome_,))
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/%s_3.png"%(nome_,))
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../dot/ot.dot")

f=open("../rdf/ot.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/ot.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

#########

nome_="legenda"
A=gas["legenda"][1]
g=gas["legenda"][0]
nome=("../figs/%s.png"%(nome_,))
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/%s_2.png"%(nome_,))
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/%s_3.png"%(nome_,))
A.draw(nome,prog="fdp") # draw to png using circo



sys.exit()


