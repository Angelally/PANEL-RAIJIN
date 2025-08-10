# backend/app/models/image.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON, Float, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from sqlalchemy import Enum
from ..core.database import Base


class ProcessingStatus(PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ImageFormat(PyEnum):
    JPEG = "jpeg"
    PNG = "png"
    WEBP = "webp"
    BMP = "bmp"
    TIFF = "tiff"


class ProcessedImage(Base):
    __tablename__ = "processed_images"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # File information
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=False)  # in bytes
    mime_type = Column(String(50), nullable=False)
    format = Column(Enum(ImageFormat), nullable=False)
    
    # Image dimensions
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    
    # Processing information
    status = Column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING, nullable=False)
    processing_type = Column(String(50), nullable=False)  # cleanup, enhance, ocr, etc.
    processing_options = Column(JSON, nullable=True)  # Processing parameters
    
    # Results
    output_path = Column(String(500), nullable=True)
    output_size = Column(Integer, nullable=True)
    processing_time = Column(Float, nullable=True)  # in seconds
    quality_score = Column(Float, nullable=True)  # 0-100
    
    # OCR Results (if applicable)
    extracted_text = Column(Text, nullable=True)
    text_confidence = Column(Float, nullable=True)
    detected_language = Column(String(10), nullable=True)
    
    # Metadata
    metadata = Column(JSON, nullable=True)
    error_message = Column(Text, nullable=True)
    
    # Timestamps
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    
    # Status flags
    is_public = Column(Boolean, default=False, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="processed_images")

