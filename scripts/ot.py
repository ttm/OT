import rdflib as r, pygraphviz as gv, sys, import percolation as pe
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal
ot = r.Namespace("http://purl.org/socialparticipation/ot/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL
xsd = r.namespace.XSD


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

ga=g,A=pe.makeBasicGraph()
g.namespace_manager.bind("ot", "http://purl.org/socialparticipation/ot/")    
pe.C(ga,)




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

