from datetime import datetime

from pydantic import BaseModel


class UsersBase(BaseModel):
    phone: str
    created_at: datetime
    is_active: bool


class UsersCreate(UsersBase):
    pass


class Users(UsersBase):
    id: int

    class Config:
        from_attributes = True


class OTPRequest(BaseModel):
    phone: str


class ForgotPasswordRequest(BaseModel):
    phone: str


class OTPResponse(BaseModel):
    otp: str
    message: str


class OTPVerifyRequest(BaseModel):
    phone: str
    otp: str


class JWTTokenResponse(BaseModel):
    access_token: str
    token_type: str
    message: str


class OTPBase(BaseModel):
    phone: str
    otp: str
    created_at: datetime
    expired_at: datetime


class OTP(OTPBase):
    id: int

    class Config:
        from_attributes = True


class ChangePasswordResponse(BaseModel):
    access_token: str
    token_type: str
    message: str
