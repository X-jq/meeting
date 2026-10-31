"""API 依赖注入"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session_factory

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """获取数据库 Session，请求结束自动提交/回滚"""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()