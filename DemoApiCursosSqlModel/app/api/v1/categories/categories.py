from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.database import get_session
from app.models.categories.category import Categories, CategoriesCreate, CategoriesRead, CategoryeBase, CategoryUpdate 

router = APIRouter()

@router.post("/", response_model=CategoriesRead)
async def create_category(*, session: Session = Depends(get_session), data: CategoriesCreate):

    with session: 
        new_category = Categories.from_orm(data)
        session.add(new_category)
        session.commit()
        session.refresh(new_category)
        return new_category


@router.get("/", response_model=list[CategoriesRead])
async def get_categories(*, session: Session = Depends(get_session)): 
    
    with session:
        categories = session.exec(select(Categories)).all()
        return categories


@router.get("/limit", response_model=list[CategoriesRead])
async def get_categories_limit(*, offset: int = 0, limit: int = 10, session: Session = Depends(get_session)): 
    
    with session:
        categories = session.exec(select(Categories).offset(offset).limit(limit)).all()
        return categories   


@router.get("/find/{id}", response_model=CategoriesRead)
async def find_category(id: int, session: Session = Depends(get_session)): 
    
    with session:
        category = session.exec(select(Categories).where(Categories.id == id)).first()
        return category    

    
@router.get("/find/{name}", response_model=CategoriesRead)
async def find_category_name(name: str, session: Session = Depends(get_session)): 
    
    with session:
        category = session.exec(select(Categories).where(Categories.name == name)).first()
        return category  
    

@router.put("/{id}", response_model=CategoriesRead)
async def update_category_by_id(id: int, updated_category: CategoryUpdate, session: Session = Depends(get_session)):
   
    with session:
        category = session.get(Categories, id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        
        category.name = updated_category.name
        
        session.add(category)
        session.commit()
        session.refresh(category)
        
        return category


@router.delete("/{id}")
async def delete_category_by_id(id: int,  session: Session = Depends(get_session)):
   
    with session:
        category = session.get(Categories, id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        
        session.delete(category)
        session.commit()
        
        return {"message": f"Category with ID {id} deleted successfully"}    