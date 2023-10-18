import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.fave import *
from vkbottle_types.responses.base import OkResponse


class FaveCategory(BaseCategory):
    async def add_article(
        self,
        url: str,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addArticle method


        :param url:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_link(
        self,
        link: str,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addLink method


        :param link: Link URL.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addPage method


        :param user_id:
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_post(
        self,
        owner_id: int,
        id: int,
        access_key: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addPost method


        :param owner_id:
        :param id:
        :param access_key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_product(
        self,
        owner_id: int,
        id: int,
        access_key: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addProduct method


        :param owner_id:
        :param id:
        :param access_key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_tag(
        self,
        name: typing.Optional[str] = None,
        position: typing.Optional[str] = "back",
        **kwargs,
    ) -> FaveAddTagResponseModel:
        """fave.addTag method


        :param name:
        :param position:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = FaveAddTagResponse

        return model(**response).response

    async def add_video(
        self,
        owner_id: int,
        id: int,
        access_key: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.addVideo method


        :param owner_id:
        :param id:
        :param access_key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_tag(
        self,
        id: int,
        name: str,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.editTag method


        :param id:
        :param name:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[True] = True,
        item_type: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 50,
        fields: typing.Optional[str] = None,
        is_from_snackbar: typing.Optional[bool] = None,
        **kwargs,
    ) -> FaveGetExtendedResponseModel:
        ...

    async def get(
        self,
        extended: typing.Optional[bool] = 0,
        item_type: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 50,
        fields: typing.Optional[str] = None,
        is_from_snackbar: typing.Optional[bool] = None,
        **kwargs,
    ) -> FaveGetResponseModel:
        """fave.get method


        :param extended: '1' - to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param is_from_snackbar:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), FaveGetExtendedResponse),),
            default=FaveGetResponse,
            params=params,
        )

        return model(**response).response

    async def get_pages(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 50,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        tag_id: typing.Optional[int] = None,
        **kwargs,
    ) -> FaveGetPagesResponseModel:
        """fave.getPages method


        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = FaveGetPagesResponse

        return model(**response).response

    async def get_tags(
        self,
        **kwargs,
    ) -> FaveGetTagsResponseModel:
        """fave.getTags method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = FaveGetTagsResponse

        return model(**response).response

    async def mark_seen(
        self,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """fave.markSeen method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def remove_article(
        self,
        owner_id: int,
        article_id: int,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """fave.removeArticle method


        :param owner_id:
        :param article_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def remove_link(
        self,
        link_id: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removeLink method


        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_page(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removePage method


        :param user_id:
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_post(
        self,
        owner_id: int,
        id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removePost method


        :param owner_id:
        :param id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_product(
        self,
        owner_id: int,
        id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removeProduct method


        :param owner_id:
        :param id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_tag(
        self,
        id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removeTag method


        :param id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_video(
        self,
        owner_id: int,
        id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.removeVideo method


        :param owner_id:
        :param id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def reorder_tags(
        self,
        ids: typing.List[int],
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.reorderTags method


        :param ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_page_tags(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.setPageTags method


        :param user_id:
        :param group_id:
        :param tag_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_tags(
        self,
        item_type: typing.Optional[str] = None,
        item_owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        link_id: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.setTags method


        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def track_page_interaction(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """fave.trackPageInteraction method


        :param user_id:
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("FaveCategory",)
