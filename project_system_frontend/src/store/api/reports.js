import {RENTIHA_PATH} from "../../helpers/urls";
import baseApi from "./baseApiEndpoints";

// Define a service using a base URL and expected endpoints
export const authApi = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    getAllReports: builder.query({
      query: () => `${RENTIHA_PATH}`,
        providesTags: ['Reports']
    }),
    reportUpdate: builder.mutation({
      query: (payload) => ({
        url: `${RENTIHA_PATH}${payload?.id}/`,
        method: "PATCH",
        body: payload
      }),
      invalidatesTags: ['Reports']
    }),
    reportCreate: builder.mutation({
      query: (payload) => ({
        url: `${RENTIHA_PATH}`,
        method: "POST",
        body: payload
      }),
      invalidatesTags: ['Reports']
    }),
    reportRemove: builder.mutation({
      query: (id) => ({
        url: `${RENTIHA_PATH}${id}/`,
        method: "DELETE",
      }),
      invalidatesTags: ['Reports']
    }),
  }),
  overrideExisting: false,
});

export const { useGetAllReportsQuery, useReportUpdateMutation, useReportCreateMutation, useReportRemoveMutation } = authApi;
