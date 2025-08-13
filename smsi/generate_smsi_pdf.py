from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import datetime


def build_pdf(output_path: str) -> None:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=1, spaceAfter=16))
    styles.add(ParagraphStyle(name="H1", parent=styles["Heading1"], spaceBefore=12, spaceAfter=8))
    styles.add(ParagraphStyle(name="H2", parent=styles["Heading2"], spaceBefore=10, spaceAfter=6))
    styles.add(ParagraphStyle(name="H3", parent=styles["Heading3"], spaceBefore=8, spaceAfter=4))
    styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], leading=14))
    # Utiliser le style Bullet existant fourni par ReportLab (éviter la redéfinition)
    styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=9, leading=12, textColor=colors.grey))

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Guide pratique SMSI (ISO/IEC 27001:2022)",
        author="Généré par un assistant IA",
        subject="Exercices, cas pratiques, méthodes et gabarits pour un SMSI efficace",
    )

    story = []

    # Page de garde
    story.append(Paragraph("Guide pratique SMSI (ISO/IEC 27001:2022)", styles["TitleCenter"]))
    story.append(Paragraph("Exercices, cas pratiques et méthodes pour devenir Lead Implementer opérationnel", styles["H2"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"Version 1.0 — {datetime.now().strftime('%d/%m/%Y')}", styles["Small"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Ce document propose une feuille de route, des exercices guidés, des cas pratiques et des gabarits prêts à l'emploi pour mettre en place un SMSI conforme à l'ISO/IEC 27001:2022. ",
        styles["Body"],
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Note: Ce guide est pédagogique et ne remplace pas la lecture des normes ISO applicables (27001, 27002, 27005, 27003, 27007). Adaptez toujours les exemples à votre contexte.",
        styles["Small"],
    ))
    story.append(PageBreak())

    # Feuille de route
    story.append(Paragraph("Feuille de route d'implémentation (vue macro)", styles["H1"]))
    roadmap_points = [
        "Engagement de la direction, désignation du sponsor, charte de projet et gouvernance (comités, rôles, RACI).",
        "Compréhension du contexte et des parties intéressées; exigences légales, réglementaires et contractuelles.",
        "Définition du périmètre du SMSI et des frontières: sites, systèmes, processus, exclusions justifiées.",
        "Politique de sécurité de l'information et objectifs mesurables (KPI/OKR).",
        "Inventaire des actifs informationnels, classification et propriétaires.",
        "Méthode d'appréciation du risque (ISO 27005/EBIOS RM), critères d'acceptation et matrice d'impact/probabilité.",
        "Appréciation des risques, plan de traitement, coûts, priorités et échéances.",
        "Déclaration d'Applicabilité (SoA) alignée sur l'Annexe A (93 contrôles de l'édition 2022).",
        "Mise en œuvre des contrôles, politiques, procédures et enregistrements requis.",
        "Sensibilisation et formation; gestion du changement, communication et conduite du projet.",
        "Surveillance et mesure: indicateurs, journaux, tableaux de bord, tests, audits internes.",
        "Revue de direction, actions correctives, amélioration continue (PDCA) et préparation à la certification.",
    ]
    for p in roadmap_points:
        story.append(Paragraph(p, styles["Bullet"], bulletText="-"))
    story.append(Spacer(1, 12))

    # Jeu d'exercices progressif
    story.append(Paragraph("Jeu d'exercices progressif (livrables attendus)", styles["H1"]))

    def exercise(title: str, objectifs: list, consignes: list, livrables: list):
        story.append(Paragraph(title, styles["H2"]))
        story.append(Paragraph("Objectifs", styles["H3"]))
        for it in objectifs:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Consignes", styles["H3"]))
        for it in consignes:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Livrables", styles["H3"]))
        for it in livrables:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Spacer(1, 8))

    exercise(
        "Exercice 1 — Contexte et parties intéressées",
        [
            "Analyser le contexte interne/externe et identifier les parties intéressées et leurs attentes.",
            "Lister les exigences applicables (légales, réglementaires, contractuelles).",
        ],
        [
            "Réaliser une analyse SWOT et (optionnel) PESTEL sur l'organisation choisie (réelle ou fictive).",
            "Dresser la liste des parties intéressées et de leurs exigences pertinentes.",
        ],
        [
            "Note de contexte (1-2 pages).",
            "Registre des parties intéressées et exigences associées.",
        ],
    )

    exercise(
        "Exercice 2 — Périmètre du SMSI",
        [
            "Définir un périmètre clair et justifier les exclusions.",
            "Identifier les processus, sites, systèmes et services couverts.",
        ],
        [
            "Rédiger un énoncé de périmètre incluant frontières, interfaces, dépendances et hypothèses.",
            "Valider le périmètre avec la direction (simulation de validation).",
        ],
        [
            "Énoncé de périmètre (scope statement) prêt à approuver.",
        ],
    )

    exercise(
        "Exercice 3 — Inventaire et classification des actifs",
        [
            "Établir un inventaire structuré des actifs informationnels.",
            "Attribuer des propriétaires et une classification (ex: Public, Interne, Confidentiel).",
        ],
        [
            "Lister actifs: informations, applications, matériels, services, personnes, fournisseurs.",
            "Associer criticité et impacts (disponibilité, intégrité, confidentialité).",
        ],
        [
            "Registre des actifs avec classification et propriétaire.",
        ],
    )

    exercise(
        "Exercice 4 — Critères d'acceptation et matrice de cotation",
        [
            "Définir les niveaux d'impact et de probabilité, et le seuil d'acceptation du risque.",
        ],
        [
            "Construire une grille 1-5 pour Impact et Probabilité (adaptée à votre contexte).",
            "Définir les bandes de risque (faible, moyen, élevé).",
        ],
        [
            "Politique de gestion des risques (critères et matrice).",
        ],
    )

    exercise(
        "Exercice 5 — Appréciation des risques (ISO 27005 / EBIOS RM)",
        [
            "Identifier menaces et vulnérabilités, évaluer risques et prioriser.",
        ],
        [
            "Sélectionner 5 scénarios de risque significatifs et calculer le niveau de risque initial.",
            "Proposer des options de traitement (réduire, éviter, transférer, accepter).",
        ],
        [
            "Registre des risques avec calculs et priorités.",
        ],
    )

    exercise(
        "Exercice 6 — Plan de traitement des risques (PTR)",
        [
            "Définir les mesures, les responsables, les budgets, les délais et les dépendances.",
        ],
        [
            "Établir un PTR sur 3-6 mois avec jalons, coûts et bénéfices.",
            "Préparer une présentation de validation pour le comité de pilotage.",
        ],
        [
            "PTR validé et calendrier de déploiement.",
        ],
    )

    exercise(
        "Exercice 7 — Déclaration d'Applicabilité (SoA)",
        [
            "Documenter l'applicabilité des 93 contrôles de l'Annexe A et leur statut.",
        ],
        [
            "Justifier inclusion/exclusion pour chaque contrôle et référencer la documentation associée.",
        ],
        [
            "SoA versionnée et approuvée.",
        ],
    )

    exercise(
        "Exercice 8 — Politiques et procédures clés",
        [
            "Produire les politiques minimales et 3-5 procédures critiques.",
        ],
        [
            "Rédiger: Politique de SI, Politique de classification, Politique contrôle d'accès.",
            "Rédiger 3-5 procédures: gestion incidents, sauvegardes, gestion changements, gestion logs, MDM.",
        ],
        [
            "Corpus documentaire versionné, contrôlé et diffusé.",
        ],
    )

    exercise(
        "Exercice 9 — Sensibilisation et formation",
        [
            "Structurer un programme de sensibilisation sur 12 mois.",
        ],
        [
            "Planifier campagnes, supports, évaluations et suivi du taux de complétion.",
        ],
        [
            "Programme annuel, contenus et indicateurs (ex: taux de réussite > 85%).",
        ],
    )

    exercise(
        "Exercice 10 — KPI et tableaux de bord",
        [
            "Définir des objectifs mesurables et les instruments de mesure.",
        ],
        [
            "Sélectionner 8-12 indicateurs (ex: MTTR incidents, patching SLA, pourcentage comptes avec MFA).",
        ],
        [
            "Tableau de bord mensuel du SMSI (visuel simple).",
        ],
    )

    exercise(
        "Exercice 11 — Programme d'audit interne",
        [
            "Planifier un programme couvrant clauses 4-10 et Annexe A sur 12 mois.",
        ],
        [
            "Construire des checklists, critères, périmètres et méthodes d'échantillonnage.",
        ],
        [
            "Programme d'audit, checklists, rapports et suivi d'actions.",
        ],
    )

    exercise(
        "Exercice 12 — Revue de direction et préparation certification",
        [
            "Consolider l'état du SMSI et préparer l'audit externe.",
        ],
        [
            "Collecter preuves, indicateurs, résultats d'audits, NC et actions, décisions SoA.",
        ],
        [
            "Dossier de revue de direction, registre d'actions et plan de remédiation.",
        ],
    )

    # Exemples de grilles et tableaux
    story.append(Paragraph("Exemples de grilles et gabarits", styles["H1"]))

    story.append(Paragraph("Matrice de cotation (exemple)", styles["H2"]))
    headers = ["Critère", "1", "2", "3", "4", "5"]
    data = [
        headers,
        ["Impact (CIA)", "Mineur", "Modéré", "Significatif", "Majeur", "Critique"],
        ["Probabilité", "Très rare", "Peu probable", "Possible", "Probable", "Très probable"],
        ["Tolérance", "Acceptable", "Acceptable", "Surveiller", "Réduire", "Réduire/Avoid"],
    ]
    tbl = Table(data, colWidths=[4.2 * cm] + [2.3 * cm] * 5)
    tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Gabarit de registre des risques (exemple de colonnes)", styles["H2"]))
    risk_cols = [
        "ID", "Actif/Processus", "Scénario de risque", "Menaces/Vulnérabilités", "Impact", "Prob.", "Niveau initial",
        "Option traitement", "Contrôles (Annexe A)", "Niveau résiduel", "Propriétaire", "Échéance"
    ]
    risk_tbl = Table([risk_cols], colWidths=[1.2*cm, 3.2*cm, 4.2*cm, 3.8*cm, 1.5*cm, 1.5*cm, 2.5*cm, 3.0*cm, 3.8*cm, 2.5*cm, 2.8*cm, 2.5*cm])
    risk_tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))
    story.append(risk_tbl)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Gabarit de Déclaration d'Applicabilité (SoA) — colonnes clés", styles["H2"]))
    soa_cols = [
        "ID contrôle", "Intitulé (Annexe A)", "Applicable ?", "Justification", "Statut", "Références (polis/proc)"
    ]
    soa_tbl = Table([soa_cols], colWidths=[2.0*cm, 6.5*cm, 2.5*cm, 6.5*cm, 2.5*cm, 5.0*cm])
    soa_tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))
    story.append(soa_tbl)
    story.append(PageBreak())

    # Cas pratiques
    story.append(Paragraph("Cas pratiques (scénarios types)", styles["H1"]))

    def case_block(title: str, contexte: list, perimetre: list, risques: list, controles: list, kpis: list, livrables: list):
        story.append(Paragraph(title, styles["H2"]))
        story.append(Paragraph("Contexte", styles["H3"]))
        for it in contexte:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Périmètre", styles["H3"]))
        for it in perimetre:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Principaux scénarios de risque", styles["H3"]))
        for it in risques:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Contrôles phares (Annexe A 2022)", styles["H3"]))
        for it in controles:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("KPI recommandés", styles["H3"]))
        for it in kpis:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Paragraph("Livrables attendus", styles["H3"]))
        for it in livrables:
            story.append(Paragraph(it, styles["Bullet"], bulletText="-"))
        story.append(Spacer(1, 8))

    case_block(
        "PME SaaS B2B (Cloud, multi-tenant)",
        [
            "Application SaaS exposée sur Internet, clients entreprises, exigences contractuelles fortes.",
            "Environnement cloud (IaaS/PaaS), intégration CI/CD et déploiements fréquents.",
        ],
        [
            "Services applicatifs, données clients, pipeline CI/CD, gestion des secrets, fournisseurs cloud.",
        ],
        [
            "Exfiltration de données clients suite à vulnérabilité applicative (OWASP Top 10).",
            "Compromission d'identifiants et mouvements latéraux via accès à privilèges.",
            "Indisponibilité majeure due à défaillance configuration cloud (erreur humaine).",
        ],
        [
            "Gestion des identités et des accès, MFA, moindres privilèges, séparation des environnements.",
            "Durcissement du pipeline CI/CD, revue de code, tests SAST/DAST, gestion des secrets.",
            "Journalisation, détection d'incidents, sauvegardes et plans de reprise.",
        ],
        [
            "Taux de couverture MFA > 98% des comptes.",
            "Délai moyen de correction vulnérabilités critiques < 7 jours.",
            "Taux de conformité des sauvegardes restaurées > 99%.",
        ],
        [
            "SoA spécifique au cloud, politiques d'accès, procédure de gestion des vulnérabilités, PTR priorisé.",
        ],
    )

    case_block(
        "Clinique / Hôpital (données de santé)",
        [
            "Forte contrainte réglementaire (données de santé, secret médical), disponibilité critique.",
            "Parc hétérogène (SIH, imagerie, biomédical), nombreux sous-traitants.",
        ],
        [
            "SIH, dossiers patients, imagerie, réseau médical, prestataires et hébergement HDS (si applicable).",
        ],
        [
            "Ransomware impactant patients et continuité de soins.",
            "Fuite d'imagerie médicale via partages mal configurés.",
            "Interruption d'un service critique par panne et absence de PRA testé.",
        ],
        [
            "Segmentation réseau, durcissement postes biomédicaux, sauvegardes 3-2-1 et PRA testé.",
            "Gestion des prestataires, clauses contractuelles, journalisation réglementaire.",
            "Sensibilisation ciblée phishing et hygiène numérique.",
        ],
        [
            "Taux de disponibilité services critiques > 99,9%.",
            "Délai rétablissement (RTO) respecté lors des tests PRA.",
            "Taux de non-conformités fournisseurs résolues < 30 jours.",
        ],
        [
            "Cartographie applicative critique, plan de continuité, dossiers d'homologation, programme d'audit fournisseurs.",
        ],
    )

    case_block(
        "Fintech / Services financiers",
        [
            "Exigences réglementaires et d'audit élevées, tolérance au risque très faible.",
            "Forte exposition fraude et conformité (KYC/AML en périphérie).",
        ],
        [
            "Systèmes de paiement, bases clients, anti-fraude, partenaires bancaires et PSP.",
        ],
        [
            "Fraude par prise de contrôle de compte, injection de transactions non autorisées.",
            "Risque tiers sur PSP/sous-traitants critiques.",
        ],
        [
            "Contrôles d'accès renforcés, séparation des tâches, surveillance transactions, alertes en temps réel.",
            "Due diligence fournisseurs, tests de reprise, chiffrement en transit/au repos.",
        ],
        [
            "Taux d'alertes traitées < 15 min; faux positifs < 5%.",
            "Audit logs conservés 12-24 mois, intègres et exploitables.",
        ],
        [
            "Politique d'acceptation des risques, SoA complète, procédures anti-fraude et de journalisation.",
        ],
    )

    story.append(PageBreak())

    # Méthodes détaillées
    story.append(Paragraph("Méthodes et pratiques recommandées", styles["H1"]))
    methods = [
        "PDCA (Plan-Do-Check-Act): coeur de l'amélioration continue du SMSI.",
        "Gestion des risques (ISO 27005, EBIOS RM): registre des risques vivant, seuils d'acceptation, revues périodiques.",
        "Gestion documentaire: contrôle des versions, statuts, propriétaires et périodicité de revue.",
        "Gestion des accès: principes de moindre privilège, MFA, revue périodique des droits.",
        "Gestion des changements: évaluation d'impacts sécurité, approbations et traçabilité.",
        "Gestion des incidents: détection, enregistrement, classification, réponse, post-mortem et leçons apprises.",
        "Continuité d'activité: analyses d'impact (BIA), stratégies, PRA/PCA, tests réguliers.",
        "Sécurité des fournisseurs: due diligence, clauses contractuelles, revues et indicateurs.",
        "Sécurité des développements: revue de code, SAST/DAST, gestion des dépendances, secrets, SBOM.",
        "Protection des données à caractère personnel: principes, registre des traitements, minimisation, DPIA si nécessaire.",
    ]
    for m in methods:
        story.append(Paragraph(m, styles["Bullet"], bulletText="-"))

    story.append(Spacer(1, 8))

    story.append(Paragraph("Contrôles ISO/IEC 27001:2022 — thématiques (93 contrôles)", styles["H2"]))
    story.append(Paragraph(
        "Organisationnel, Humain, Physique, Technologique. Cartographiez vos contrôles internes à ces thématiques et référencez-les dans la SoA.",
        styles["Body"],
    ))

    story.append(PageBreak())

    # Annexes et gabarits
    story.append(Paragraph("Annexes et gabarits", styles["H1"]))

    story.append(Paragraph("Gabarit — Énoncé de périmètre (exemple)", styles["H2"]))
    story.append(Paragraph(
        "Le SMSI couvre: [sites, unités, processus, systèmes]. Interfaces: [internes/externes]. Exclusions: [justifiées]. Hypothèses: [liste]. Périmètre temporel: [date].",
        styles["Body"],
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Gabarit — Politique de sécurité (sections minimales)", styles["H2"]))
    for it in [
        "Objet et champ d'application",
        "Engagement de la direction",
        "Rôles et responsabilités",
        "Approche de gestion des risques",
        "Objectifs et mesures de performance",
        "Gestion documentaire et diffusion",
        "Conformité et sanctions",
    ]:
        story.append(Paragraph(it, styles["Bullet"], bulletText="-"))

    story.append(Spacer(1, 6))

    story.append(Paragraph("Checklist — Clauses 4 à 10 (exemples de questions)", styles["H2"]))
    checklist = [
        "Clause 4 (Contexte): Le périmètre et les parties intéressées sont-ils documentés et à jour?",
        "Clause 5 (Leadership): La politique est-elle communiquée et comprise?",
        "Clause 6 (Planification): Les risques et opportunités sont-ils traités? Critères définis?",
        "Clause 7 (Support): Ressources, compétences et sensibilisation sont-elles démontrées?",
        "Clause 8 (Opérations): Procédures mises en oeuvre et traces conservées?",
        "Clause 9 (Évaluation): Indicateurs, audits internes et revue de direction réalisés?",
        "Clause 10 (Amélioration): NC traitées dans les délais, leçons apprises capitalisées?",
    ]
    for q in checklist:
        story.append(Paragraph(q, styles["Bullet"], bulletText="-"))

    story.append(Spacer(1, 8))

    story.append(Paragraph("Liens utiles (références publiques)", styles["H2"]))
    refs = [
        '<a href="https://www.ssi.gouv.fr/entreprise/ebios-risk-manager/">ANSSI — EBIOS Risk Manager</a>',
        '<a href="https://www.nist.gov/">NIST — Publications (ex: SP 800-61, SP 800-53)</a>',
        '<a href="https://owasp.org/www-project-top-ten/">OWASP Top 10</a>',
        '<a href="https://www.cisecurity.org/controls">CIS Critical Security Controls</a>',
        '<a href="https://cloudsecurityalliance.org/research/cloud-controls-matrix">CSA Cloud Controls Matrix</a>',
    ]
    for r in refs:
        story.append(Paragraph(r, styles["Body"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Mentions: Les marques et normes citées appartiennent à leurs propriétaires respectifs. Document éducatif.",
        styles["Small"],
    ))

    # Build
    doc.build(story)


if __name__ == "__main__":
    output_file = "/workspace/smsi/Guide_pratique_SMSI_ISO27001.pdf"
    build_pdf(output_file)
    print(f"PDF généré: {output_file}")