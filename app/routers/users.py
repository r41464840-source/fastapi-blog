from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import oauth2


from .. import models, schemas
from ..database import get_db
from ..utils.hashing import hash_password, verify_password


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# CREATE USER
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bu email allaqachon ro'yxatdan o'tgan"
        )

    hashed = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.get("/me", response_model=schemas.UserResponse)
def get_current_user_info(
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return current_user




# GET USER
@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={user_id} bo'lgan foydalanuvchi topilmadi"
        )

    return user



@router.put("/change-password")
def change_password(
    password_data: schemas.PasswordChange,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    # Проверяем старый пароль
    if not verify_password(
        password_data.old_password,
        current_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Eski parol noto'g'ri"
        )

    # Хешируем новый пароль
    current_user.password = hash_password(
        password_data.new_password
    )

    db.commit()

    return {"message": "Parol muvaffaqiyatli o'zgartirildi"}
