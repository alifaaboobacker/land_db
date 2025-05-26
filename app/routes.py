from flask import Blueprint, request, send_file, jsonify
from .models import LandRecord
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

land_blueprint = Blueprint('land', __name__)

@land_blueprint.route('/search', methods=['GET'])
def search_land():
    from .models import db
    query = request.args.get('q')
    record = LandRecord.query.filter(
        (LandRecord.parcel_id == query) | 
        (LandRecord.plot_number == query) | 
        (LandRecord.owner_name.ilike(f"%{query}%"))
    ).first()

    if not record:
        return jsonify({'error': 'Record not found'}), 404

    # Generate PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_file:
        c = canvas.Canvas(pdf_file.name, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Land Record Summary")
        c.drawString(100, 730, f"Parcel ID: {record.parcel_id}")
        c.drawString(100, 710, f"Plot Number: {record.plot_number}")
        c.drawString(100, 690, f"Owner Name: {record.owner_name}")
        c.drawString(100, 670, f"Area: {record.area}")
        c.drawString(100, 650, f"Location: {record.location}")
        c.drawString(100, 630, f"Registration Date: {record.registration_date}")
        c.save()

        return send_file(pdf_file.name, as_attachment=True, download_name='land_record.pdf')
