# backend/app/models/settings.py
from sqlalchemy import Column, Integer, String, Text, JSON, Boolean, DateTime
from sqlalchemy.sql import func
from ..core.database import Base


class SystemSetting(Base):
    __tablename__ = "system_settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, index=True, nullable=False)
    value = Column(Text, nullable=True)
    data_type = Column(String(20), default="string", nullable=False)  # string, int, float, bool, json
    category = Column(String(50), default="general", nullable=False)
    description = Column(Text, nullable=True)
    
    # Metadata
    is_public = Column(Boolean, default=False, nullable=False)  # Can be read by non-admin users
    is_readonly = Column(Boolean, default=False, nullable=False)  # Cannot be modified via API
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())