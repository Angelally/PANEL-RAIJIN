# backend/app/models/activity.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from sqlalchemy import Enum
from ..core.database import Base


class ActivityType(PyEnum):
    LOGIN = "login"
    LOGOUT = "logout"
    REGISTER = "register"
    IMAGE_UPLOAD = "image_upload"
    IMAGE_PROCESS = "image_process"
    PROFILE_UPDATE = "profile_update"
    PASSWORD_CHANGE = "password_change"
    ADMIN_ACTION = "admin_action"
    SYSTEM_EVENT = "system_event"


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Can be null for system events
    
    # Activity details
    action = Column(Enum(ActivityType), nullable=False)
    resource = Column(String(100), nullable=True)  # What was affected
    resource_id = Column(String(50), nullable=True)  # ID of the affected resource
    
    # Request information
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    method = Column(String(10), nullable=True)  # HTTP method
    endpoint = Column(String(255), nullable=True)
    
    # Details and metadata
    description = Column(Text, nullable=True)
    metadata = Column(JSON, nullable=True)  # Additional structured data
    
    # Status
    success = Column(Boolean, default=True, nullable=False)
    error_message = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="activities")