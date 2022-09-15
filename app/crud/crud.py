# from typing import Union, List
# from sqlalchemy.orm import Session
# from app.crud.gmc_service import GmcService
# from app.database.models import models
# from app.database.schemas import gmc_schema, comment_schema
# from fastapi import HTTPException
# from sqlalchemy.orm import Query
# from fastapi import Query as FastapiQuery


# def build_gmc_query(
#         db: Session,
#         domain: Union[str, None] = None,
#         status: Union[str, None] = None,
#         merchant_id: Union[str, None] = None,
#         email: Union[str, None] = None,
#         site_type: Union[str, None] = None,
#         theme: Union[str, None] = None,
#         merchant_status: Union[List[str], None] = FastapiQuery(default=None),
#         proxy_ip: Union[str, None] = None,
#         server_ip: Union[str, None] = None,
#         profile_name: Union[str, None] = None,
#         created_by: Union[str, None] = None,
#         ) -> Query:
#     query = db.query(gmcs.Gmc)
#     if domain:
#         query = query.filter(gmcs.Gmc.domain == domain)
#     if status:
#         query = query.filter(gmcs.Gmc.status == status)
#     if merchant_id:
#         query = query.filter(gmcs.Gmc.merchant_id == merchant_id)
#     if email:
#         query = query.filter(gmcs.Gmc.email == email)
#     if site_type:
#         query = query.filter(gmcs.Gmc.site_type == site_type)
#     if theme:
#         query = query.filter(gmcs.Gmc.theme == theme)

#     if merchant_status:
#         query = query.filter(gmcs.Gmc.merchant_status.in_(merchant_status))

#     elif merchant_status == "any":
#         pass
#     if proxy_ip:
#         query = query.filter(gmcs.Gmc.proxy_ip == proxy_ip)
#     if server_ip:
#         query = query.filter(gmcs.Gmc.server_ip == server_ip)
#     if profile_name:
#         query = query.filter(gmcs.Gmc.profile_name == profile_name)
#     if created_by:
#         query = query.filter(gmcs.Gmc.created_by == created_by)
#     return query


# def get(
#      db: Session,
#         domain: Union[str, None] = None,
#         status: Union[str, None] = None,
#         merchant_id: Union[str, None] = None,
#         email: Union[str, None] = None,
#         site_type: Union[str, None] = None,
#         theme: Union[str, None] = None,
#         merchant_status: Union[List[str], None] = FastapiQuery(default=None),
#         proxy_ip: Union[str, None] = None,
#         server_ip: Union[str, None] = None,
#         profile_name: Union[str, None] = None,
#         created_by: Union[str, None] = None,
#         page: int = 1,
#         per_page: int = 20
#         ) -> List[models.Users]:
#     per_page = GmcService.validate_page(parameters=per_page)
#     page = GmcService.validate_page(parameters=page, page=True)
#     query = build_gmc_query(
#             db=db,
#             domain=domain,
#             status=status,
#             merchant_id=merchant_id,
#             email=email,
#             site_type=site_type,
#             theme=theme,
#             merchant_status=merchant_status,
#             proxy_ip=proxy_ip,
#             server_ip=server_ip,
#             profile_name=profile_name,
#             created_by=created_by
#             )
#     query = query.order_by(gmcs.Gmc.id.desc())
#     query = query.offset((page - 1) * per_page).limit(per_page)
#     gmc_query = query.all()
#     return gmc_query



