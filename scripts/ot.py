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

ga=pe.makeBasicGraph()
ga[0].namespace_manager.bind("ot", "http://purl.org/socialparticipation/ot/")    


pe.C([ga],ot.Physics,
     "Física",
     comment=["the natural science that involves the study of matter, its motion through space and time, and related concepts such as energy and force. More broadly, it is the general analysis of nature, conducted in order to understand how the universe behaves.","""Mathematics is the language used for compact description of the order in nature, especially the laws of physics. This was noted and advocated by Pythagoras, Plato, Galileo, and Newton.
     Physics theories use mathematics to obtain order and provide precise formulas, precise or estimated solutions, quantitative results and predictions. Experiment results in physics are numerical measurements. Technologies based on mathematics, like computation have made computational physics an active area of research.
     Ontology is a prerequisite for physics, but not for mathematics. It means physics is ultimately concerned with descriptions of the real world, while mathematics is concerned with abstract patterns, even beyond the real world. Thus physics statements are synthetic, while mathematical statements are analytic. Mathematics contains hypotheses, while physics contains theories. Mathematics statements have to be only logically true, while predictions of physics statements must match observed and experimental data."""],
     label_en="Physics")



pe.C([ga],ot.StatisticalPhysics,u"Física Estatística",
        superclass=ot.Physics,
        comment="Branch of physics that uses methods of probability theory and statistics",label_en="Statistical Physics")

pe.C([ga],ot.ComplexNetworksTheory,u"Teoria das Redes Complexas",superclass=ot.StatisticalPhysics,
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
     superclass=ot.SocialNetwork,
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
     "Física Antropológica",
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
     "Participação Social",
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
     "Dados Ligados",
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
        "Tese de Doutorado",
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


sys.exit()


# Templates:
#cl=ot.Probability
#lcl3=lcl=u""
#A.add_node(lcl,style="filled")
#nd=A.get_node(lcl)
#nd.attr['color']="#A29999"
#
#G(cl,rdf.type,owl.Class)
#G(cl,rdfs.label,L(lcl,lang="pt"))
#G(cl,rdfs.label,L(u"",lang="en"))



comNet=cl=ot.ComplexNetworks
lcl1=lcl=u"Redes Complexas"
A.add_node(lcl,style="filled")
nd=A.get_node(lcl)
nd.attr['color']="#A29999"

G(cl,rdf.type,owl.Class)
G(cl,rdfs.label,L(lcl,lang="pt"))
G(cl,rdfs.label,L(u"Complex Networks",lang="en"))
#G(cl,rdfs.comment,L(lcl,lang="pt"))

####

cl=ot.GraphTheory
lcl2=lcl=u"Teoria de Grafos"
A.add_node(lcl,style="filled")
nd=A.get_node(lcl)
nd.attr['color']="#A29999"

G(cl,rdf.type,owl.Class)
G(cl,rdfs.label,L(lcl,lang="pt"))
G(cl,rdfs.label,L(u"Graph Theory",lang="en"))
#G(cl,rdfs.comment,L(lcl,lang="pt"))

####

cl=ot.Probability
lcl3=lcl=u"Probabilidade"
A.add_node(lcl,style="filled")
nd=A.get_node(lcl)
nd.attr['color']="#A29999"

G(cl,rdf.type,owl.Class)
G(cl,rdfs.label,L(lcl,lang="pt"))
G(cl,rdfs.label,L(u"Probability",lang="en"))

####

grounds=prop=ot.grounds
lprop=u"fundamenta"
G(prop,rdf.type,owl.ObjectProperty)
G(prop,rdfs.label,L(lprop,lang="pt"))

A.add_edge(lcl2,lcl1)
e=A.get_edge(lcl2,lcl1)
e.attr["label"]=lprop

A.add_edge(lcl3,lcl2)
e=A.get_edge(lcl3,lcl2)
e.attr["label"]=lprop

####

cl=ot.StatisticalPhysics
lcl=lcl=u"Física Estatística"
A.add_node(lcl,style="filled")
nd=A.get_node(lcl)
nd.attr['color']="#A29999"

G(cl,rdf.type,owl.Class)
G(cl,rdfs.label,L(lcl,lang="pt"))
G(cl,rdfs.label,L(u"Statistical Physics",lang="en"))

####

G(comNet,rdfs.subClassOf,cl)
A.add_edge(lcl1,lcl)
e=A.get_edge(lcl1,lcl)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

####

prop=ot.enables
lprop=u"possibilita"
G(prop,rdf.type,owl.ObjectProperty)
G(grounds, rdfs.subPropertyOf,prop)
G(prop,rdfs.label,L(lprop,lang="pt"))

####

cl=ot.Probability
lcl3=lcl=u"Probabilidade"
A.add_node(lcl,style="filled")
nd=A.get_node(lcl)
nd.attr['color']="#A29999"

G(cl,rdf.type,owl.Class)
G(cl,rdfs.label,L(lcl,lang="pt"))
G(cl,rdfs.label,L(u"Probability",lang="en"))




####




nome=("../figs/ot.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/ot2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/ot3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../dot/ot.dot")

f=open("../rdf/ot.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/ot.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()



sys.exit()
cgu=obs.CGU
lcgu=u"Controladoria-Geral da União (CGU)" # entra no SKOS
G(cgu,rdf.type,owl.Class)
G(cgu,rdfs.label,L(lcgu,lang="pt"))
A.add_node(lcgu,style="filled") ###

uni=obs.unit
luni=u"unidade"
Uni=obs.SFC
lUni=u"Secretaria Federal de Controle Interno (SFC)"
G(uni,rdf.type,owl.ObjectProperty)
G(uni,rdfs.label,L(luni,lang="pt"))
G(Uni,rdf.type,owl.Class)
G(Uni,rdfs.label,L(lUni,lang="pt"))
A.add_node(lUni,style="filled")
A.add_edge(lcgu,lUni)
e=A.get_edge(lcgu,lUni)
e.attr["label"]=luni

uni2=obs.competence
luni2=u"competência"
Uni2=obs.Audit
lUni2=u"Auditoria"
G(uni2,rdf.type,owl.ObjectProperty)
G(uni2,rdfs.label,L(luni2,lang="pt"))
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.Regulation
lUni2=u"Normatização"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.Standardization
lUni2=u"Padronização"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.PublicPatrimonyDefense
lUni2=u"Defesa de patrimônio público"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2



Uni=obs.CRG
lUni=u"Corregedoria-Geral da União (CRG)"
G(Uni,rdf.type,owl.Class)
G(Uni,rdfs.label,L(lUni,lang="pt"))
A.add_node(lUni,style="filled")
A.add_edge(lcgu,lUni)
e=A.get_edge(lcgu,lUni)
e.attr["label"]=luni

Uni2=obs.Correction
lUni2=u"Correção"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2



Uni=obs.STPC
lUni=u"Secretaria de Transparência e Prevenção à Corrupção (STPC)"
G(Uni,rdf.type,owl.Class)
G(Uni,rdfs.label,L(lUni,lang="pt"))
A.add_node(lUni,style="filled")
A.add_edge(lcgu,lUni)
e=A.get_edge(lcgu,lUni)
e.attr["label"]=luni

Uni2=obs.Transparency
lUni2=u"Transparência"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.Prevention
lUni2=u"Prevenção"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2





A.add_edge(lcgu,louv)
e=A.get_edge(lcgu,louv)
e.attr["label"]=luni

lUni=louv
Uni2=obs.FederalOmbudsmanCoordination
lUni2=u"Coordenação de ouvidoria do poder executivo federal"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.MessageReception
lUni2=u"Recepção de mensagens"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.ComplaintReception
lUni2=u"Recepção de denúncias"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.ComplaintForwarding
lUni2=u"Encaminhamento de denúncias"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.ManifestationReception
lUni2=u"Recepção de manifestações referentes a serviços públicos"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.ManifestationAnalysis
lUni2=u"Análise de manifestações referentes a serviços públicos"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2

Uni2=obs.InformationAccessResponse
lUni2=u"Resposta a pedido de acesso à informação"
G(Uni2,rdf.type,owl.Class)
G(Uni2,rdfs.label,L(lUni2,lang="pt"))
A.add_node(lUni2,style="filled")
A.add_edge(lUni,lUni2)
e=A.get_edge(lUni,lUni2)
e.attr["label"]=luni2








####

ativa=obs.ativa # SKOS
lativa=u"ativa"
G(ativa,rdf.type,owl.DatatypeProperty)
G(ativa,rdfs.label,L(lativa,lang="pt"))
G(ativa,rdfs.comment,L(u"ouvidoria é ativa?",lang="pt"))
G(ativa,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(louv,COUNT)
e=A.get_edge(louv,COUNT); COUNT+=1
e.attr["label"]=lativa

responsavel=obs.accountable
lresponsavel=u"responsável"
Ouvidor=obs.Ombudsman
lOuvidor=u"Ouvidor"
G(responsavel,rdf.type,owl.ObjectProperty)
G(responsavel,rdfs.label,L(lresponsavel,lang="pt"))
G(Ouvidor,rdf.type,owl.Class)
G(Ouvidor,rdfs.label,L(lOuvidor,lang="pt"))
G(responsavel,rdfs.range,Ouvidor)
A.add_node(lOuvidor,style="filled")
A.add_edge(louv,lOuvidor)
e=A.get_edge(louv,lOuvidor)
e.attr["label"]=lresponsavel

nome=obs.name
lnome=u"nome"
G(nome,rdf.type,owl.DatatypeProperty)
G(nome,rdfs.label,L(lnome,lang="pt"))
G(nome,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lOuvidor,COUNT)
e=A.get_edge(lOuvidor,COUNT); COUNT+=1
e.attr["label"]=lnome

nome=obs.telephone
lnome=u"telefone"
G(nome,rdf.type,owl.DatatypeProperty)
G(nome,rdfs.label,L(lnome,lang="pt"))
G(nome,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lOuvidor,COUNT)
e=A.get_edge(lOuvidor,COUNT); COUNT+=1
e.attr["label"]=lnome



local=obs.location
llocal=u"localização"
G(local,rdf.type,owl.DatatypeProperty)
G(local,rdfs.label,L(llocal,lang="pt"))
G(local,rdfs.comment,L(u"órgão e localização do ouvidor dentro do órgão em que trabalha",lang="pt"))
G(local,rdfs.range,xsd.string)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:string"
nd.attr['color']="#A2F3D1"
A.add_edge(lOuvidor,COUNT)
e=A.get_edge(lOuvidor,COUNT); COUNT+=1
e.attr["label"]=llocal

orgao=obs.agency
lorgao=u"órgão"
OrgaoPub=obs.PublicAgency
lOrgaoPub=u"Órgão público" # SKOS
G(orgao,rdf.type,owl.ObjectProperty)
G(orgao,rdfs.label,L(lorgao,lang="pt"))
G(OrgaoPub,rdf.type,owl.Class)
G(OrgaoPub,rdfs.label,L(lOrgaoPub,lang="pt"))
G(orgao,rdfs.range,OrgaoPub)
A.add_node(lOrgaoPub,style="filled")
A.add_edge(louv,lOrgaoPub)
e=A.get_edge(louv,lOrgaoPub)
e.attr["label"]=lorgao

A.add_edge(u"Ouvidor",lOrgaoPub)
e=A.get_edge(u"Ouvidor",lOrgaoPub)
e.attr["label"]=lorgao



sp=obs.PublicAdministrationAgency
lsp=u"Órgão da administração pública" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
lsp_=lsp

sp=obs.Hospital
lsp=u"Hospital" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Ministry
lsp=u"Ministério" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,obs.PublicAdministrationAgency)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lsp_)
e=A.get_edge(lsp,lsp_)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2




sp=obs.University
lsp=u"Universidade" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


G(cgu,rdfs.subClassOf,OrgaoPub)
A.add_edge(lcgu,lOrgaoPub)
e=A.get_edge(lcgu,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


sp=obs.IndirectPublicAdministrationAgency
lsp=u"Órgão da administração pública indireta" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,OrgaoPub)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOrgaoPub)
e=A.get_edge(lsp,lOrgaoPub)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2
lsp__=lsp
sp__=sp

sp=obs.Foundation
lsp=u"Fundação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,sp__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lsp__)
e=A.get_edge(lsp,lsp__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


sj=obs.shouldJoin
lsj=u"integrará" # SKOS
Ou=obs.OmbudsmanNationalSystem
lOu=u"Sistema Federal de Ouvidorias"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,Ou)
A.add_node(lOu,style="filled")
A.add_edge(louv,lOu)
e=A.get_edge(louv,lOu)
e.attr["label"]=lsj

sp=obs.SAC
lsp=u"SAC (Sistema de Atendimento ao Cidadão)" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(ouv,rdfs.subClassOf,sp)
A.add_node(lsp,style="filled") ###
A.add_edge(louv,lsp)
e=A.get_edge(louv,lsp)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sj=obs.articulates
lsj=u"articula" # SKOS
Ou=obs.OGU
lOu=u"OGU (Ouvidoria Geral da União)"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(lOu,louv)
e=A.get_edge(lOu,louv)
e.attr["label"]=lsj


sj=obs.delivers
lsj=u"entrega" # SKOS
Ou=obs.Report
lOu=u"Relatório"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(louv,lOu)
e=A.get_edge(louv,lOu)
e.attr["label"]=lsj
lOu_=lOu


nm=obs.periodicity
lnm=u"peridodicidade"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.integer)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:integer"
nd.attr['color']="#A2F3D1"
A.add_edge(  lOu,COUNT)
e=A.get_edge(lOu,COUNT); COUNT+=1
e.attr["label"]=lnm


sj=obs.guides
lsj=u"orienta" # SKOS
Ou=obs.Control
lOu=u"Controle"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.range,ouv)
A.add_node(lOu,style="filled")
A.add_edge(lOu_,lOu)
e=A.get_edge(lOu_,lOu)
e.attr["label"]=lsj

sp=obs.InternalControl
lsp=u"Controle interno" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.ExternalControl
lsp=u"Controle externo" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.CivilControl
lsp=u"Controle civil" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sj=obs.dialogues
lsj=u"dialoga" # SKOS
pm__=obs.ParticipationInstanceOrMechanism # SKOS
lpm__=u"Instância ou mecanismo de participação social"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj

sj=obs.incorporates
lsj=u"incorpora" # SKOS
pm__=obs.LAI# SKOS
lpm__=u"LAI (Lei de Acesso à Informação)" # SKOS
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj


sj=obs.receives
lsj=u"recebe" # SKOS
pm__=obs.Manifestation # SKOS
lpm__=u"Manifestação" # SKOS
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm__)
G(pm__,rdf.type,owl.Class)
G(pm__,rdfs.label,L(lpm__,lang="pt"))
A.add_node(lpm__,style="filled")
A.add_edge(louv,lpm__)
e=A.get_edge(louv,lpm__)
e.attr["label"]=lsj

sj=obs.author
lsj=u"autor" # SKOS
pm___=obs.Participant # SKOS
lpm___=u"Participante" # SKOS
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(sj,rdfs.range,pm___)
G(pm___,rdf.type,owl.Class)
G(pm___,rdfs.label,L(lpm___,lang="pt"))
A.add_node(lpm___,style="filled")
A.add_edge(lpm__,lpm___)
e=A.get_edge(lpm__,lpm___)
e.attr["label"]=lsj

sp=obs.Whistleblower
lsp=u"Denunciante" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm___)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm___)
e=A.get_edge(lsp,lpm___)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Client
lsp=u"Cliente" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm___)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm___)
e=A.get_edge(lsp,lpm___)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Contributor
lsp=u"Contribuidor" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm___)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm___)
e=A.get_edge(lsp,lpm___)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Rioter
lsp=u"Manifestante" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm___)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm___)
e=A.get_edge(lsp,lpm___)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.NotOrganizedCivilSociety
lsp=u"Sociedade civil não organizada" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm___)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm___)
e=A.get_edge(lsp,lpm___)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2










sp=obs.Request
lsp=u"Solicitação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Complaint
lsp=u"Reclamação" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Compliment
lsp=u"Elogio" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Suggestion
lsp=u"Sugestão" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Denunciation
lsp=u"Denúncia" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,pm__)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp,lpm__)
e=A.get_edge(lsp,lpm__)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

nm=obs.identityReservation
lnm=u"reserva de identidade"
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(  lpm__,COUNT)
e=A.get_edge(lpm__,COUNT); COUNT+=1
e.attr["label"]=lnm

nm=obs.anonymous
lnm=u"anônima" # SKOS
G(nm,rdf.type,owl.DatatypeProperty)
G(nm,rdfs.label,L(lnm,lang="pt"))
G(nm,rdfs.range,xsd.boolean)
A.add_node(COUNT,style="filled")
nd=A.get_node(COUNT)
nd.attr["label"]="xsd:boolean"
nd.attr['color']="#A2F3D1"
A.add_edge(  lpm__,COUNT)
e=A.get_edge(lpm__,COUNT); COUNT+=1
e.attr["label"]=lnm

# 
sj=obs.qualifies
lsj=u"qualifica" # SKOS
Ou=obs.FormationActivity
lOu=u"Atividade de formação"
G(sj,rdf.type,owl.ObjectProperty)
G(sj,rdfs.label,L(lsj,lang="pt"))
G(Ou,rdf.type,owl.Class)
G(Ou,rdfs.label,L(lOu,lang="pt"))
G(sj,rdfs.domain,Ou)
A.add_node(lOu,style="filled")
A.add_edge(lOu,louv)
e=A.get_edge(lOu,louv)
e.attr["label"]=lsj

sp=obs.Lecture
lsp=u"Palestra" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Course
lsp=u"Curso" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2

sp=obs.Seminar
lsp=u"Seminário" # entra no SKOS
G(sp,rdf.type,owl.Class)
G(sp,rdfs.label,L(lsp,lang="pt"))
G(sp,rdfs.subClassOf,Ou)
A.add_node(lsp,style="filled") ###
A.add_edge(lsp  ,lOu)
e=A.get_edge(lsp,lOu)
e.attr["arrowhead"]="empty"
e.attr["arrowsize"]=2


nome=("../figs/obsOuvidoria.png")
A.draw(nome,prog="dot") # draw to png using circo
nome=("../figs/obsOuvidoria2.png")
A.draw(nome,prog="circo") # draw to png using circo
nome=("../figs/obsOuvidoria3.png")
A.draw(nome,prog="fdp") # draw to png using circo
A.write("../dot/obsOuvidoria.dot")

f=open("../rdf/obsOuvidoria.owl","wb")
f.write(g.serialize())
f.close()
f=open("../rdf/obsOuvidoria.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()

