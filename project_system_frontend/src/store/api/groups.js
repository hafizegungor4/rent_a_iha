import {RENTSTATE_PATH} from "../../helpers/urls";
import baseApi from "./baseApiEndpoints";

// Define a service using a base URL and expected endpoints
export const api = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    getAllGroups: builder.query({
      query: () => `${RENTSTATE_PATH}`,
        providesTags: ['Groups']
    }),
    getGroupById: builder.query({
      query: (id) => `${RENTSTATE_PATH}${id}/`,
      providesTags: ['Groups']
    }),
    groupUpdate: builder.mutation({
      query: (payload) => ({
        url: `${RENTSTATE_PATH}${payload?.id}/`,
        method: "PATCH",
        body: payload
      }),
      invalidatesTags: ['Groups']
    }),
    groupCreate: builder.mutation({
      query: (payload) => ({
        url: `${RENTSTATE_PATH}`,
        method: "POST",
        body: payload
      }),
      invalidatesTags: ['Groups']
    }),
    groupRemove: builder.mutation({
      query: (id) => ({
        url: `${RENTSTATE_PATH}${id}/`,
        method: "DELETE",
      }),
      invalidatesTags: ['Groups']
    }),
  }),
  overrideExisting: false,
});

export const { useGetAllGroupsQuery, useGetGroupByIdQuery, useGroupUpdateMutation, useGroupCreateMutation, useGroupRemoveMutation } = api;
