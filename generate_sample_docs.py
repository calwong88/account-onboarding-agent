"""
Generate realistic sample PDF documents for the Richardson Family Trust scenario.
These simulate the kinds of documents a private banking accounts processing team
would receive from a high-net-worth client onboarding.
"""

import os
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "sample_docs", "richardson_trust")


def get_styles():
    """Create custom paragraph styles for professional-looking documents."""
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="DocTitle", parent=styles["Title"],
        fontSize=16, spaceAfter=20, textColor=HexColor("#1a1a2e"),
    ))
    styles.add(ParagraphStyle(
        name="DocSubtitle", parent=styles["Normal"],
        fontSize=11, spaceAfter=12, textColor=HexColor("#555555"),
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name="SectionHead", parent=styles["Heading2"],
        fontSize=12, spaceBefore=16, spaceAfter=8,
        textColor=HexColor("#1a1a2e"),
    ))
    styles.add(ParagraphStyle(
        name="BodyText2", parent=styles["Normal"],
        fontSize=10, leading=15, alignment=TA_JUSTIFY,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="SmallText", parent=styles["Normal"],
        fontSize=8, textColor=HexColor("#888888"),
    ))
    return styles


def create_trust_agreement():
    """
    Generate a Trust Agreement PDF that intentionally has a flaw:
    it references Schedule B (Beneficiaries) but does NOT include it.
    This simulates a real-world issue the validation engine should catch.
    """
    filepath = os.path.join(OUTPUT_DIR, "Richardson_Trust_Agreement_2024.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            topMargin=1*inch, bottomMargin=0.75*inch)
    styles = get_styles()
    story = []

    # Title page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("DECLARATION OF TRUST", styles["DocTitle"]))
    story.append(Paragraph("The Richardson Family Trust", styles["DocSubtitle"]))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Established: March 15, 2019", styles["DocSubtitle"]))
    story.append(Paragraph("Trust Jurisdiction: Province of Ontario, Canada", styles["DocSubtitle"]))
    story.append(Spacer(1, 1*inch))

    trust_info = [
        ["Settlor:", "Margaret Richardson"],
        ["Trustees:", "Michael Richardson, Diana Richardson"],
        ["Trust Type:", "Inter Vivos Discretionary Family Trust"],
        ["Date of Settlement:", "March 15, 2019"],
        ["Initial Settlement:", "$100.00 CAD"],
    ]
    t = Table(trust_info, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TEXTCOLOR", (0, 0), (0, -1), HexColor("#555555")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(PageBreak())

    # Article 1
    story.append(Paragraph("ARTICLE 1 — DEFINITIONS AND INTERPRETATION", styles["SectionHead"]))
    story.append(Paragraph(
        '1.1 In this Trust Agreement, "Beneficiaries" means those persons listed in '
        'Schedule B attached hereto, as may be amended from time to time by the Trustees '
        'in accordance with the powers granted herein.',
        styles["BodyText2"]
    ))
    story.append(Paragraph(
        '1.2 "Trust Property" means all property transferred to, or acquired by, the '
        'Trustees to be held in trust pursuant to this Declaration, including all income, '
        'gains, and proceeds therefrom.',
        styles["BodyText2"]
    ))
    story.append(Paragraph(
        '1.3 "Trustees" means Michael Richardson and Diana Richardson, and any '
        'successor trustee appointed in accordance with Article 5.',
        styles["BodyText2"]
    ))

    # Article 2
    story.append(Paragraph("ARTICLE 2 — DECLARATION OF TRUST", styles["SectionHead"]))
    story.append(Paragraph(
        "2.1 The Settlor hereby transfers to the Trustees the sum of One Hundred Dollars "
        "($100.00 CAD) to be held by the Trustees upon the trusts and subject to the "
        "powers and provisions set out in this Declaration of Trust.",
        styles["BodyText2"]
    ))
    story.append(Paragraph(
        "2.2 The Trustees may accept further property of any kind from any person to be "
        "held as Trust Property on the same trusts and subject to the same provisions.",
        styles["BodyText2"]
    ))

    # Article 3
    story.append(Paragraph("ARTICLE 3 — DISTRIBUTIONS", styles["SectionHead"]))
    story.append(Paragraph(
        "3.1 The Trustees may, in their absolute discretion, pay, apply, or distribute "
        "all or any part of the income and/or capital of the Trust Property to or for "
        "the benefit of any one or more of the Beneficiaries, in such amounts and at "
        "such times as the Trustees see fit.",
        styles["BodyText2"]
    ))
    story.append(Paragraph(
        "3.2 Any income of the Trust not distributed in the year in which it is earned "
        "shall be accumulated and added to the capital of the Trust.",
        styles["BodyText2"]
    ))

    # Article 4
    story.append(Paragraph("ARTICLE 4 — POWERS OF TRUSTEES", styles["SectionHead"]))
    story.append(Paragraph(
        "4.1 The Trustees shall have the following powers in addition to any powers "
        "conferred by law: (a) to invest Trust Property in any form of investment, "
        "including but not limited to real property, equities, fixed income securities, "
        "private equity, and alternative investments; (b) to borrow money on behalf of "
        "the Trust; (c) to open and maintain bank accounts and investment accounts at "
        "any financial institution; (d) to retain professional advisors.",
        styles["BodyText2"]
    ))

    # Article 5
    story.append(Paragraph("ARTICLE 5 — TRUSTEE SUCCESSION", styles["SectionHead"]))
    story.append(Paragraph(
        "5.1 A Trustee may resign by providing 60 days written notice to the remaining "
        "Trustee(s). 5.2 A successor Trustee may be appointed by a majority of the "
        "remaining Trustees, or if no Trustee remains, by a majority of the adult "
        "Beneficiaries.",
        styles["BodyText2"]
    ))

    # Schedule A (included) — this is fine
    story.append(PageBreak())
    story.append(Paragraph("SCHEDULE A — INITIAL TRUST PROPERTY", styles["SectionHead"]))
    story.append(Paragraph(
        "The initial trust property settled upon the Trust by the Settlor is the sum of "
        "One Hundred Dollars ($100.00 CAD), receipt of which is hereby acknowledged by "
        "the Trustees.",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(
        "Additional property subsequently transferred to the Trust:",
        styles["BodyText2"]
    ))
    additions = [
        ["Date", "Description", "Approximate Value"],
        ["June 10, 2019", "Portfolio of publicly traded securities", "$2,400,000 CAD"],
        ["September 3, 2020", "Residential real property — 178 Forest Hill Rd", "$3,100,000 CAD"],
        ["January 15, 2022", "Additional cash contribution", "$500,000 CAD"],
    ]
    t = Table(additions, colWidths=[1.5*inch, 3*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f0f0f0")),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    # NOTE: Schedule B (Beneficiaries) is intentionally OMITTED
    # This is the flaw the validation engine should detect

    # Signature page
    story.append(PageBreak())
    story.append(Paragraph("EXECUTION", styles["SectionHead"]))
    story.append(Paragraph(
        "IN WITNESS WHEREOF, the parties have executed this Declaration of Trust "
        "as of the 15th day of March, 2019.",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 0.5*inch))

    sig_data = [
        ["_________________________", "", "_________________________"],
        ["Margaret Richardson", "", "Michael Richardson"],
        ["Settlor", "", "Trustee"],
        ["", "", ""],
        ["", "", "_________________________"],
        ["", "", "Diana Richardson"],
        ["", "", "Trustee"],
    ]
    t = Table(sig_data, colWidths=[2.5*inch, 0.5*inch, 2.5*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGNMENT", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(t)

    doc.build(story)
    print(f"  ✓ Trust Agreement ({os.path.basename(filepath)})")
    return filepath


def create_passport():
    """Generate a simulated passport data page for trustee Michael Richardson."""
    filepath = os.path.join(OUTPUT_DIR, "M_Richardson_Passport.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            topMargin=1*inch, bottomMargin=0.75*inch)
    styles = get_styles()
    story = []

    story.append(Paragraph("CANADA — PASSPORT / PASSEPORT", styles["DocTitle"]))
    story.append(HRFlowable(width="100%", thickness=2, color=HexColor("#cc0000")))
    story.append(Spacer(1, 0.3*inch))

    passport_data = [
        ["Type / Type:", "P"],
        ["Country Code / Code du pays:", "CAN"],
        ["Surname / Nom:", "RICHARDSON"],
        ["Given Names / Prénoms:", "MICHAEL JAMES"],
        ["Nationality / Nationalité:", "CANADIAN / CANADIENNE"],
        ["Date of Birth / Date de naissance:", "1972-04-18"],
        ["Sex / Sexe:", "M"],
        ["Place of Birth / Lieu de naissance:", "TORONTO, ON"],
        ["Date of Issue / Date de délivrance:", "2023-09-14"],
        ["Date of Expiry / Date d'expiration:", "2028-09-14"],
        ["Passport No. / No de passeport:", "GA 847291"],
        ["Address / Adresse:", "42 Rosedale Road, Toronto, ON M4W 2P5"],
    ]
    t = Table(passport_data, colWidths=[2.8*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (0, -1), HexColor("#333333")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc")))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "P&lt;CANRICHARDSON&lt;&lt;MICHAEL&lt;JAMES&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;",
        styles["SmallText"]
    ))
    story.append(Paragraph(
        "GA847291&lt;6CAN7204185M2809146&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;04",
        styles["SmallText"]
    ))

    doc.build(story)
    print(f"  ✓ Passport ({os.path.basename(filepath)})")
    return filepath


def create_source_of_wealth():
    """
    Generate a Source of Wealth declaration that is intentionally vague.
    It says 'business income' but doesn't specify the business name or nature.
    The validation engine should flag this under enhanced due diligence rules.
    """
    filepath = os.path.join(OUTPUT_DIR, "Source_of_Wealth_Declaration.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            topMargin=1*inch, bottomMargin=0.75*inch)
    styles = get_styles()
    story = []

    story.append(Paragraph("SOURCE OF WEALTH DECLARATION", styles["DocTitle"]))
    story.append(Paragraph("BMO Private Banking — Know Your Client", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor("#0055a4")))
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("Section 1 — Declarant Information", styles["SectionHead"]))
    info = [
        ["Full Legal Name:", "The Richardson Family Trust"],
        ["Account Type:", "Trust"],
        ["Trustee(s):", "Michael Richardson, Diana Richardson"],
        ["Date:", datetime.now().strftime("%B %d, %Y")],
    ]
    t = Table(info, colWidths=[2*inch, 4.3*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    story.append(Paragraph("Section 2 — Primary Source of Wealth", styles["SectionHead"]))
    story.append(Paragraph(
        "Please indicate the primary source(s) of wealth for the trust and/or its settlor:",
        styles["BodyText2"]
    ))

    # Intentionally vague — should be flagged
    sources = [
        ["☑", "Business Income"],
        ["☐", "Employment Income"],
        ["☐", "Inheritance"],
        ["☐", "Investment Returns"],
        ["☑", "Real Estate"],
        ["☐", "Sale of Business"],
        ["☐", "Other (specify): _______________"],
    ]
    t = Table(sources, colWidths=[0.4*inch, 5*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Section 3 — Additional Details", styles["SectionHead"]))
    story.append(Paragraph(
        "Please provide additional details regarding the source(s) of wealth indicated above, "
        "including the name and nature of any business, the approximate total net worth, and "
        "any relevant supporting documentation.",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 0.1*inch))
    # Intentionally vague answer — no business name or details
    story.append(Paragraph(
        "The trust's wealth originates primarily from business income generated over "
        "several decades, as well as real estate holdings in the Greater Toronto Area. "
        "Approximate total net worth of trust assets: $6,000,000 CAD.",
        styles["BodyText2"]
    ))

    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Section 4 — Declaration", styles["SectionHead"]))
    story.append(Paragraph(
        "I/We, the undersigned, declare that the information provided above is true and "
        "accurate to the best of my/our knowledge. I/We understand that BMO may request "
        "additional documentation to verify the source of wealth.",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("_________________________", styles["BodyText2"]))
    story.append(Paragraph("Michael Richardson, Trustee", styles["BodyText2"]))
    story.append(Paragraph(datetime.now().strftime("%B %d, %Y"), styles["SmallText"]))

    doc.build(story)
    print(f"  ✓ Source of Wealth Declaration ({os.path.basename(filepath)})")
    return filepath


def create_utility_bill():
    """
    Generate a utility bill for proof of address that is intentionally
    slightly too old (94 days) — just past the 90-day policy limit.
    Also uses a DIFFERENT address from the passport to trigger cross-ref alert.
    """
    # Bill date is 94 days ago — just past the 90-day limit
    bill_date = datetime.now() - timedelta(days=94)

    filepath = os.path.join(OUTPUT_DIR, "Hydro_Bill_Richardson.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            topMargin=1*inch, bottomMargin=0.75*inch)
    styles = get_styles()
    story = []

    story.append(Paragraph("TORONTO HYDRO", styles["DocTitle"]))
    story.append(HRFlowable(width="100%", thickness=2, color=HexColor("#00a651")))
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("ELECTRICITY BILL / FACTURE D'ÉLECTRICITÉ", styles["DocSubtitle"]))
    story.append(Spacer(1, 0.2*inch))

    # Note: address is 178 Forest Hill Rd — different from passport (42 Rosedale Rd)
    bill_info = [
        ["Account Holder:", "Michael Richardson"],
        ["Service Address:", "178 Forest Hill Road, Toronto, ON M5P 2N5"],
        ["Account Number:", "4520-8891-7234"],
        ["Bill Date:", bill_date.strftime("%B %d, %Y")],
        ["Due Date:", (bill_date + timedelta(days=21)).strftime("%B %d, %Y")],
        ["Billing Period:", f"{(bill_date - timedelta(days=30)).strftime('%b %d')} — {bill_date.strftime('%b %d, %Y')}"],
    ]
    t = Table(bill_info, colWidths=[2*inch, 4.3*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.3*inch))

    charges = [
        ["Description", "Amount"],
        ["Electricity Charges", "$142.37"],
        ["Delivery Charges", "$68.21"],
        ["Regulatory Charges", "$12.84"],
        ["Debt Retirement Charge", "$0.00"],
        ["HST (13%)", "$29.04"],
        ["Total Amount Due", "$252.46"],
    ]
    t = Table(charges, colWidths=[4*inch, 2*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#e8f5e9")),
        ("BACKGROUND", (0, -1), (-1, -1), HexColor("#e8f5e9")),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    doc.build(story)
    print(f"  ✓ Utility Bill ({os.path.basename(filepath)})")
    return filepath


def create_crs_self_cert():
    """Generate a CRS/FATCA Tax Residency Self-Certification for the trust."""
    filepath = os.path.join(OUTPUT_DIR, "CRS_Trust_SelfCert.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            topMargin=1*inch, bottomMargin=0.75*inch)
    styles = get_styles()
    story = []

    story.append(Paragraph("TAX RESIDENCY SELF-CERTIFICATION", styles["DocTitle"]))
    story.append(Paragraph("Common Reporting Standard (CRS) / FATCA — Entity", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor("#0055a4")))
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("Part 1 — Identification of Account Holder (Entity)", styles["SectionHead"]))
    info = [
        ["Legal Name of Entity:", "The Richardson Family Trust"],
        ["Country of Incorporation/Establishment:", "Canada"],
        ["Registered Address:", "178 Forest Hill Road, Toronto, ON M5P 2N5"],
        ["Mailing Address:", "Same as above"],
    ]
    t = Table(info, colWidths=[2.8*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    story.append(Paragraph("Part 2 — Entity Type", styles["SectionHead"]))
    entity_types = [
        ["☑", "Passive Non-Financial Entity (Passive NFE) — Trust"],
        ["☐", "Active Non-Financial Entity (Active NFE)"],
        ["☐", "Financial Institution"],
        ["☐", "International Organization"],
    ]
    t = Table(entity_types, colWidths=[0.4*inch, 5.5*inch])
    t.setStyle(TableStyle([("FONTSIZE", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story.append(t)

    story.append(Paragraph("Part 3 — Country of Tax Residence", styles["SectionHead"]))
    tax_info = [
        ["Country of Tax Residence:", "Canada"],
        ["Tax Identification Number (TIN):", "T-2019-RF-84523"],
        ["GIIN (if applicable):", "N/A — Non-Financial Entity"],
    ]
    t = Table(tax_info, colWidths=[2.8*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)

    story.append(Paragraph("Part 4 — FATCA Classification", styles["SectionHead"]))
    story.append(Paragraph(
        "The entity is not a U.S. person and is not a Specified U.S. Person. "
        "The entity does not have any U.S. indicia.",
        styles["BodyText2"]
    ))

    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Part 5 — Declaration and Signature", styles["SectionHead"]))
    story.append(Paragraph(
        "I certify that the information provided above is true, correct, and complete. "
        "I undertake to notify BMO Private Banking of any change in circumstances that "
        "would affect the tax residency status of this entity.",
        styles["BodyText2"]
    ))
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph("_________________________", styles["BodyText2"]))
    story.append(Paragraph("Michael Richardson, Trustee", styles["BodyText2"]))
    story.append(Paragraph(datetime.now().strftime("%B %d, %Y"), styles["SmallText"]))

    doc.build(story)
    print(f"  ✓ CRS Self-Certification ({os.path.basename(filepath)})")
    return filepath


def main():
    """Generate all sample documents for the Richardson Trust scenario."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\nGenerating sample documents in: {OUTPUT_DIR}\n")

    files = []
    files.append(create_trust_agreement())
    files.append(create_passport())
    files.append(create_source_of_wealth())
    files.append(create_utility_bill())
    files.append(create_crs_self_cert())

    print(f"\n✓ Generated {len(files)} sample documents.")
    print(f"\nIntentional flaws embedded for validation testing:")
    print(f"  • Trust Agreement: Schedule B (Beneficiaries) is missing")
    print(f"  • Source of Wealth: Says 'business income' but no business name/details")
    print(f"  • Utility Bill: Dated 94 days ago (exceeds 90-day policy limit)")
    print(f"  • Passport vs Utility Bill: Different addresses (42 Rosedale vs 178 Forest Hill)")
    print(f"  • Trust names TWO trustees but only ONE passport is submitted")
    print(f"  • Missing: Beneficiary Schedule, Trustee Resolution, Trust Tax ID")


if __name__ == "__main__":
    main()
