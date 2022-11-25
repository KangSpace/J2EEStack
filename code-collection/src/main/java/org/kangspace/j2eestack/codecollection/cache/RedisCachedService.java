package org.kangspace.j2eestack.codecollection.cache;


/**
 * Redis缓存Service
 *
 * @author kango2gler@gmail.com
 * @since 2022/10/28
 */
public interface RedisCachedService<RedisTemplateValueType,KEY_PATTERN> extends CachedService<KEY_PATTERN> {

    /**
     * 获取RedisTemplate
     *
     * @return {@link RedisTemplate}
     */
    <RedisTemplate,String, RedisTemplateValueType> RedisTemplate redisTemplate();

    @Override
    default  <T> T getCacheValue(String key) {
        return (T) key;
    }

    @Override
    default <T> Boolean setCacheValue(String key, T value, Long ttlSeconds) {
        return true;
    }

    @Override
    default Boolean clearCache(String key){
//        redisTemplate().delete(key);
        return true;
    }
}
