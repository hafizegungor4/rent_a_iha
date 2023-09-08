import {IHA_PATH} from "../../helpers/urls";
import baseApi from "./baseApiEndpoints";

// Define a service using a base URL and expected endpoints
export const authApi = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    getAllCourses: builder.query({
      query: () => `${IHA_PATH}`,
        providesTags: ['Courses']
    }),
    courseUpdate: builder.mutation({
      query: (payload) => ({
        url: `${IHA_PATH}${payload?.id}/`,
        method: "PATCH",
        body: payload
      }),
      invalidatesTags: ['Courses']
    }),
    courseCreate: builder.mutation({
      query: (payload) => ({
        url: `${IHA_PATH}`,
        method: "POST",
        body: payload
      }),
      invalidatesTags: ['Courses']
    }),
    courseRemove: builder.mutation({
      query: (id) => ({
        url: `${IHA_PATH}${id}/`,
        method: "DELETE",
      }),
      invalidatesTags: ['Courses']
    }),
  }),
  overrideExisting: false,
});

export const { useGetAllCoursesQuery, useCourseUpdateMutation, useCourseCreateMutation, useCourseRemoveMutation } = authApi;
